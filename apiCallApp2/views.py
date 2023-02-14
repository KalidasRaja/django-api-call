from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from algoliasearch_django import raw_search
from .models import facilityData

from algoliasearch.search_client import SearchClient


def index(request):
    params = {"hitsPerPage": 5}
    response = raw_search(facilityData, "0768267366", params)
    # print(response)
    return JsonResponse(response)
    # return render(request, 'index.html', {'data' : response})

def indexEndPoint(request):
    url = "https://E262GTSHGZ-dsn.algolia.net/1/indexes/Makhzny_v1_unit_search?hitsPerPage=1000"
    headers = {
        "X-Algolia-API-Key" : "85cb265e1f70d6e209a15fe716fd8e1b",
        "X-Algolia-Application-Id" : "E262GTSHGZ"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    context = {
        'data' : data['hits']
    }
    # print("Response from APIEndPoint: ", data['hits'])

    return render(request, 'index.html', context)


def client(request, query="", filters=""):
    client = SearchClient.create("E262GTSHGZ", "85cb265e1f70d6e209a15fe716fd8e1b")
    # Search the index and print the results

    index = client.init_index("Makhzny_v1_unit_search")
    # results = index.search("Self Storage Dammam", {
    #     'attributesToRetrieve': [
    #         'storageType.name',
    #         'location.name',
    #     ],
    #     'hitsPerPage': 10
    # })
    # query = {
    #     'filters' : ''
    # }
    # results = index.search_for_facet_values('', '', query)
    results = index.search(query, {'filters' : filters})


    return JsonResponse(results)



import json
import requests
import math
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

ALGOLIA_APP_ID = 'E262GTSHGZ'
ALGOLIA_API_KEY = '85cb265e1f70d6e209a15fe716fd8e1b'
LOCATION_NAME = 'location.name'
STORAGE_TYPE_NAME = 'storageType.name'
BUILDING_NAME = 'building.name'
UNIT_TYPE_NAME = 'unitType.name'


# class apisearch(TemplateView):
#     template_name = 'search.html'
#
#     def search_all(request):
#         query = request.GET.get('query')
#         filters = request.GET.get('filters')
#         facets = request.GET.get('facets')
#
#         headers = {
#             'X-Algolia-Application-Id': ALGOLIA_APP_ID,
#             'X-Algolia-API-Key': ALGOLIA_API_KEY
#         }
#         params = {
#             'query': query,
#             'filters': filters,
#             'facets': facets,
#             'page': request.GET.get('page', 0),
#             # 'hitsPerPage': request.GET.get('hitsPerPage', 130)
#         }
#         print(params)
#         response_all = requests.get(
#             'https://{}.algolia.net/1/indexes/{}'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX),
#             headers=headers,
#             params=params
#         )
#         results_all = response_all.json()
#         context = {
#             'data_hits': results_all['hits'],
#             'data_all': results_all
#         }
#         print(response_all)
#         return context
#

def search(request, query='', filters=''):
    headers = {
        'X-Algolia-Application-Id': ALGOLIA_APP_ID,
        'X-Algolia-API-Key': ALGOLIA_API_KEY,
    }
    params = {
        'filters': filters,
        'query': query
    }
    # print("param: ",params)
    url = 'https://{}.algolia.net/1/indexes/{}'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX)
    # print('URL :', url)
    response = requests.get(
        url,
        headers=headers,
        params=params,
    )
    # print(response.url)
    data = response.json()
    print("Response: ",data)

    return  JsonResponse(data)


    # return render(request, 'search.html', {'data' : data['hits']})

# def tenant_switch (request):
#     UNIT_SEARCH_INDEX = 'Makhzny_v1_unit_search'
#     if request.method == "POST":
#         globals(); UNIT_SEARCH_INDEX
#         data = request.POST
#         action = data.get("Makhzny_v1_unit_search")
#         if action == "Makhzny_v1_unit_search":
#             UNIT_SEARCH_INDEX = 'Makhzny_v1_unit_search'
#             print(UNIT_SEARCH_INDEX)
#         else:
#             UNIT_SEARCH_INDEX = "123Minilager_v1_unit_search"
#             print(UNIT_SEARCH_INDEX)
#     return UNIT_SEARCH_INDEX


def search_view(request, name):
    UNIT_SEARCH_INDEX = name
    query = request.GET.get('query')
    filters = request.GET.get('filters')
    facets = request.GET.get('facets')
    hitsperpage = request.GET.get('hitsPerPage', 25)
    pages = request.GET.get("page", 1)

    headers = {
        'X-Algolia-Application-Id': ALGOLIA_APP_ID,
        'X-Algolia-API-Key': ALGOLIA_API_KEY
    }
    params = {
        'query': query,
        'filters': filters,
        'facets': facets,
        'page': int(pages) - 1,
        # 'offset': (pages - 1) * 10
        'hitsPerPage': hitsperpage
    }
    response_all = requests.get(
            'https://{}.algolia.net/1/indexes/{}'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX),
            headers=headers,
            params=params
    )

    url = 'https://{}.algolia.net/1/indexes/{}'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX)
    response_all_test = requests.request('get', url=url, headers=headers, params=params)

    # print("Test :", response_all.json())
    results_all = response_all.json()
    # rr = results_all['nbPages']
    # print(rr)

    # paginator = Paginator(results_all['hits'], 10)
    # page_obj = paginator.page(pages)
    #
    # try:
    #     page_number = int(pages)
    # except ValueError:
    #     # If page number is not a number, set it to 1
    #     page_number = 0
    #
    #     # Redirect to first page if page number is less than 1
    # if page_number < 0:
    #     return redirect('search_view', page=0)
    #
    #     # Get results for the page
    # results = get_results(page_number)
    #
    # # Paginate the results
    # paginator = Paginator(results, hitsperpage)
    # try:
    #     results_page = paginator.page(page_number)
    # except PageNotAnInteger:
    #     # If page number is not an integer, show first page
    #     results_page = paginator.page(1)
    # except EmptyPage:
    #     # If page number is greater than number of pages, show last page
    #     results_page = paginator.page(paginator.num_pages)
    #
    # print("Paginator:", page_obj)


    # paginator = Paginator(results_all, hitsperpage)
    # page_obj = paginator.get_page(pages)
    # data_pagination = [{"name": kw.name} for kw in page_obj.object_list]
    # payload = {
    #     "page": {
    #         "current": page_obj.number,
    #         "has_next": page_obj.has_next(),
    #         "has_previous": page_obj.has_previous(),
    #     },
    #     "data": data_pagination
    # }
    # return JsonResponse(payload)

    response_location_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX,LOCATION_NAME ),
        headers=headers,
        data=json.dumps({}))
    results_location_facet = response_location_facet.json()

    response_storageType_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX, STORAGE_TYPE_NAME),
        headers=headers,
        data=json.dumps({}))
    results_storageType_facet = response_storageType_facet.json()

    response_building_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX, BUILDING_NAME),
        headers=headers,
        data=json.dumps({}))
    results_building_facet = response_building_facet.json()

    response_unitType_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX, UNIT_TYPE_NAME),
        headers=headers,
        data=json.dumps({}))
    results_unitType_facet = response_unitType_facet.json()

    # print(results_location_facet)
    # print(results_storageType_facet)
    # print(results_building_facet)
    # print(results_unitType_facet)
    # Prepare results for the template
    results = results_all['hits']
    total_pages = math.ceil(results_all['nbHits'] / hitsperpage)
    previous_page = int(pages) - 1 if int(pages) > 1 else None
    next_page = int(pages) + 1 if int(pages) < total_pages else None
    total_hits_per_pages = 0
    total_hits_per_pages += hitsperpage
    print(total_hits_per_pages)

    context = {
        'data_hits': results_all['hits'],
        'data_all': results_all,
        'total_hits_per_pages': total_hits_per_pages,
        'data_location_facet': results_location_facet['facetHits'],
        'data_storageType_facet': results_storageType_facet['facetHits'],
        'data_building_facet': results_building_facet['facetHits'],
        'data_unitType_facet': results_unitType_facet['facetHits'],
        UNIT_SEARCH_INDEX: 'name',
        'previous_page': previous_page,
        'next_page': next_page,
        'total_pages': total_pages,
        'current_page': pages,
        'query' : query,



    }
    # print("index",UNIT_SEARCH_INDEX)
    # print(results_all['nbPages'])
    # return render(request, 'search.html', context)
    return context
    # if request.method == 'POST':
    #     params = {
    #         'query': query,
    #         'filters': filters,
    #         'facets': facets,
    #         'page': request.GET.get('page', 0),
    #         'hitsPerPage': request.GET.get('hitsPerPage', 130)
    #     }
    #     # print(params)
    #     response = requests.post(
    #         'https://{}.algolia.net/1/indexes/{}/query'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX),
    #         headers=headers,
    #         params=params
    #     )
    #
    #     if response.status_code == 200:
    #         results = response.json()
    #         context = {
    #             'data': results['hits']
    #         }
    #         return render(request, 'search.html', context)
    #     # results = json.loads(response.text)
    #
    #     else:
    #         return render(request, 'search.html', {'error' : response.text})
    #
    # else:
    #     params = {
    #         'page': request.GET.get('page', 0),
    #         'hitsPerPage': request.GET.get('hitsPerPage', 130)
    #     }
    #     # print(params)
    #     response = requests.get(
    #         'https://{}.algolia.net/1/indexes/{}'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX),
    #         headers=headers,
    #         params=params
    #     )
    #     if response.status_code == 200:
    #         results = response.json()
    #         context = {
    #             'data': results['hits']
    #         }
    #         return render(request, 'search.html', context)
    #     # results = json.loads(response.text)
    #
    #     else:
    #         return render(request, 'search.html', {'error' : response.text})




    # print(data)
    # query = request.GET.get('query')
    # filter = request.GET.get('filters')
    # url = 'https://{}.algolia.net/1/indexes/{}/query'.format(ALGOLIA_APP_ID, UNIT_SEARCH_INDEX)
    # headers = {
    #     'X-Algolia-Application-Id': ALGOLIA_APP_ID,
    #     'X-Algolia-API-Key': ALGOLIA_API_KEY
    # }
    # params = {
    #     "query": query,
    #     "filters": filter
    # }
    # response = requests.get(url, headers=headers, params=params)
    # results = json.loads(response.text)
    # print(results)
    # return JsonResponse(results)



    # query = request.GET.get('query')
    # filters = request.GET.getlist('filters')
    # facets = request.GET.getlist('facets')
    # page = request.GET.get('page' ,'0'  )
    # # ALGOLIA_APP_ID = 'YOUR_APP_ID'
    # # ALGOLIA_API_KEY = 'YOUR_API_KEY'
    # # ALGOLIA_INDEX_NAME = 'YOUR_INDEX_NAME'
    #
    # url = f'https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{UNIT_SEARCH_INDEX}/query'
    #
    # params = {
    #     'x-algolia-api-key': ALGOLIA_API_KEY,
    #     'x-algolia-application-id': ALGOLIA_APP_ID
    # }
    #
    # data = {
    #     'query': query,
    #     'filters': ' OR '.join(filters),
    #     'attributesToRetrieve': facets,
    #     'page': page
    # }
    # response = requests.post(url, headers=params, json=data)
    # results = json.loads(response.text)
    # print("Hello Result", results)
    # return JsonResponse(results['hits'], safe=False)


def Makhzny(request):
    Makhzny = search_view(request, 'Makhzny_v1_unit_search')
    # print("Makhzny:", Makhzny)
    return render(request, 'search.html', Makhzny)


def MiniLager(request):
    MiniLager = search_view(request, '123Minilager_v1_unit_search')
    # print("MiniLager:", MiniLager)
    return render(request, 'search.html', MiniLager)