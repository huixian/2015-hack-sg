from django.db import models
from django.utils import timezone
from . import managers
#from geoposition.fields import GeopositionField

# Create your models here.

class NodeType(models.Model):
    ''' Node Type Information
    '''
    BEACON_NODE, TAG_NODE = range(2)
    NODE_CHOICES = (
            (BEACON_NODE, 'BeaconNode'),
            (TAG_NODE, 'TagNode')
        )

    type_id = models.PositiveSmallIntegerField('NodeType', blank=False)

    node_profile_type = models.PositiveSmallIntegerField(
                 default=TAG_NODE,
                 choices=NODE_CHOICES
            )

    def __str__(self):
        return ', '.join(['type ' + str(self.type_id), str(self.get_node_profile_type_display())])

class Node(models.Model):
    ''' Node Related Information
    '''
    node_id = models.IntegerField('NodeID', blank=False)

    node_type = models.ForeignKey('NodeType', blank=False, null=False,
                        related_name='node')

    node_name = models.CharField(max_length=100, blank=False, default="null")

    node_lat = models.DecimalField(max_digits=6, decimal_places=3, blank=False, default=0.0)
    node_lon = models.DecimalField(max_digits=6, decimal_places=3, blank=False, default=0.0)

    # node_location = GeopositionField(default=GeopositionField(0,0))

    def __str__(self):
        return ', '.join(['id ' + str(self.node_id), ' ' + str(self.node_type.get_node_profile_type_display()) + ', ' + str(self.node_name)])

class Reading(models.Model):
    ''' Beacon Readings
    '''

    # local timestamp on server
    # "timestamp, beaconId, tagId, tagDesc, beaconLoc" 

    server_timestamp = models.DateTimeField(auto_now_add=True)

    beacon_timestamp = models.DateTimeField(default=timezone.now())

    # sequence = models.PositiveIntegerField()

    beacon = models.ForeignKey('Node', blank=False, null=False,
                        related_name='beacon_reading')

    tag = models.ForeignKey('Node', blank=False, null=False,
                        related_name='sensor_reading')

    tagDesc = models.CharField(max_length=50, blank=True)

    beacon_lat = models.DecimalField(max_digits=6, decimal_places=3, blank=False, default=0.0)
    beacon_lon = models.DecimalField(max_digits=6, decimal_places=3, blank=False, default=0.0)

    objects = managers.ReadingsManager()

    def __str__(self):
        return ', '.join([str(self.beacon_timestamp), str(self.beacon.node_id), str(self.tag.node_id)])
