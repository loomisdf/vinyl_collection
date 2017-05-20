from django.db import models

# Create your models here.

class Album(models.Model):
    date_added = models.DateTimeField('date added to database')
    last_modified = models.DateTimeField('last time updated')

    # -1 is unknown
    # 0 is free
    # price in US dollars
    resale_value = models.DecimalField(max_digits=19, decimal_places=2)
    paid_value = models.DecimalField(max_digits=19, decimal_places=2)

    album_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    skips = models.IntegerField(default=0)

    # very poor, poor, average, good, excellent, sealed
    sleeve_quality = models.CharField(max_length=20)
    vinyl_quality = models.CharField(max_length=20)

    def description_default():
        return "";

    description = models.TextField(default=description_default)


    def __str__(self):
        return "{0}: {1}".format(self.artist_name, self.album_name)
