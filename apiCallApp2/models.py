from django.db import models


class facilityData(models.Model):
    FacilityName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    ContactNumber = models.CharField(max_length=255, blank=True)
    Country = models.CharField(max_length=255, blank=True)
    Email = models.EmailField(max_length=255)
    Plan = models.CharField(max_length=255, blank=True)
    PresonName = models.CharField(max_length=255)

    def __str__(self):
        return self.FacilityName
