from django.contrib import admin
from .models import *
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register


admin.site.register(facilityData)

@register(facilityData)
class facilityDataIndex(AlgoliaIndex):
    fields = ('FacilityName', 'City', 'ContactNumber', 'Country', 'Email', 'Plan', 'PresonName')
    # geo_field = 'location'
    settings = {'searchableAttributes': ['FacilityName', 'ContactNumber', 'Country']}
    index_name = 'facility_index'