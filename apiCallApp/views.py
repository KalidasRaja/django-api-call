from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


def user(request):
    headers = {
        "Authorization" : "Bearer 5isV+muNV9NH4aIuDf7Y01L16gBn9CiXRBpqkxibfigtYTmqYZjVxSwXzGllc7rao75T+fEbnnCtHK7/ZfUT8g==RmHrpq3beUipI3RlSVPRxQ==",
        "Content-Type" : "application/json"
    }
    body ={
        "storageTypeId": [
        ],
        "locationId": [],
        "buildingId": []
    }
    response = requests.post('https://api.8storage.com/v1/unit/storagetype/', headers = headers, json = body)
    data = response.json()
    print(data)
    print(response.status_code)

    return JsonResponse(data, safe=False)
    pass