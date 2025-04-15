from django.contrib.gis.db import models


class Marker(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return str(self.name)