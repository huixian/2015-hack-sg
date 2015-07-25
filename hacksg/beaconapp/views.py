import json
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from django.views.generic import View
from django.conf import settings
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Node, Reading
import pytz
import datetime
import time

from binascii import unhexlify, hexlify
from random import SystemRandom
import base64, binascii, struct, time
from urllib.parse import quote, unquote

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the beaconsapp index.")

def node_detail(request, node_id):
    try:
        node = Node.objects.get(node_id=node_id)
    except Node.DoesNotExist:
        raise Http404("Node does not exist")
    return HttpResponse("You're looking at node %s" % node.node_id)

@csrf_exempt
def create_reading_api(request):
    '''
    API HTTP POST call to create reading
    HTTP parameters: beacon_timestamp, beaconId, tagId, tagDesc, beacon_lat, beacon_lon
    '''

    # import pdb; pdb.set_trace()

    data = request.POST
    beacon_timestamp = int(data.get('beacon_ts', None))
    beacon_id = data.get('beacon_id', None)
    tag_id = data.get('tag_id', None)
    tag_desc = data.get('tag_desc', None)
    beacon_lat = data.get('beacon_lat', None)
    beacon_lon = data.get('beacon_lon', None)

    try:
        node_beacon = Node.objects.get(node_id=beacon_id)
    except Node.DoesNotExist:
        return HttpResponse("Beacon %s does not exist" % beacon_id, status=404)

    try:
        node_tag = Node.objects.get(node_id=tag_id)
    except Node.DoesNotExist:
        return HttpResponse("Tag %s does not exist" % tag_id, status=404)

    print("beacon_timestamp %s" % str(beacon_timestamp))
    print("node_beacon %s" % str(node_beacon.node_id))
    print("node_tag %s" % str(node_tag.node_id))
    print("tag_desc %s" % str(tag_desc))
    print("beacon loc %s, %s" % (str(beacon_lat), str(beacon_lon)))

    sys_tz = pytz.timezone(settings.TIME_ZONE)
    rx_ts = datetime.datetime.fromtimestamp(beacon_timestamp, tz=sys_tz)
    
    reading_new = Reading.objects.create_reading(rx_ts, node_beacon, node_tag, tag_desc, beacon_lat, beacon_lon) 
    
    return HttpResponse("hello %s" % beacon_id)

@csrf_exempt
def search_api(request):
    '''
    API HTTP GET call 
    '''

    data = request.GET
    tag_id = data.get('tag_id', None)
    missing_timestamp = int(data.get('missing_ts', None))

    sys_tz = pytz.timezone(settings.TIME_ZONE)
    start_time = datetime.datetime.fromtimestamp(missing_timestamp, tz=sys_tz)
    end_time = datetime.datetime.now(tz=sys_tz)

    try:
        node_tag = Node.objects.get(node_id=tag_id)
    except Node.DoesNotExist:
        return HttpResponse("Tag %s does not exist" % tag_id, status=404)

    print("tag_id %s is in database" % str(node_tag.node_id))

    reading_set = Reading.objects.filter(tag = node_tag)
    if not reading_set:
        return HttpResponse("Readings for tag_id %s does not exist" % tag_id, status=404)

    reading_set = reading_set.filter(beacon_timestamp__gte = start_time, beacon_timestamp__lt = end_time)
    if not reading_set:
        return HttpResponse("Readings for tag_id %s within time range does not exist" % tag_id, status=404)

    count = reading_set.count()

    # filter(beacon_timestamp__gte = start_time, beacon_timestamp__lt = end_time) 
    print("count %s" % str(count))
    print("start_time %s" % str(start_time))
    print("end_time %s" % str(end_time))

    payload = {}

    for elem in reading_set:
        payload[str(elem.beacon_timestamp)] = str(elem.beacon_lat) + ", " + str(elem.beacon_lon)

    return HttpResponse(json.dumps(payload), content_type="application/json")