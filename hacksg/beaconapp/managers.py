from django.db import models

class ReadingsManager(models.Manager):

	def create_reading(self, rx_ts, node_beacon, node_tag, tag_desc, beacon_lat, beacon_lon):
		print("wow")

		reading = self.create(beacon_timestamp=rx_ts, beacon=node_beacon, tag=node_tag, tagDesc=tag_desc, beacon_lat=beacon_lat, beacon_lon=beacon_lon)
		return reading