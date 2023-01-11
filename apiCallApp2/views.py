from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from algoliasearch_django import raw_search
from .models import facilityData
import requests


def index(request):
    params = {"hitsPerPage": 5}
    response = raw_search(facilityData, "0768267366", params)
    print(response)
    return JsonResponse(response)
    # return render(request, 'index.html', {'data' : response})

def indexEndPoint(request):
    url = "https://E262GTSHGZ-dsn.algolia.net/1/indexes/facility_index"
    headers = {
        "X-Algolia-API-Key" : "85cb265e1f70d6e209a15fe716fd8e1b",
        "X-Algolia-Application-Id" : "E262GTSHGZ"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print("Response from APIEndPoint: ", data['hits'] )
    return render(request, 'index.html', {'data': data['hits']})

    # return JsonResponse(data, safe=False)






