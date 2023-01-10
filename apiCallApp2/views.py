from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from algoliasearch_django import raw_search
from .models import facilityData


def index(request):
    params = {"hitsPerPage": 5}
    response = raw_search(facilityData, "0768267366", params)
    print(response)
    return JsonResponse(response)



