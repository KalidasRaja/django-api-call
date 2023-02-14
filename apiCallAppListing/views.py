from django.shortcuts import render
import json
import requests

ALGOLIA_APP_ID = 'E262GTSHGZ'
ALGOLIA_API_KEY = '85cb265e1f70d6e209a15fe716fd8e1b'
LISTING_DATA = 'cbt_listing'
FUEL = 'Fuel'
TRANSMISSION = 'Transmission'
SEATS = "Seat's"
BATTERY_COMPOSITION = 'Battery.Composition'
CHARGING_PORT = 'Charging.Charging Ports'
CHARGING_TYPE = 'Charging.Charger Type'
CHARGING_SHARING = 'Charging.Charger Sharing:'

def listing(request):
    query = request.GET.get('query')
    filters = request.GET.get('filters')
    facets = request.GET.get('facets')
    hitsperpage = request.GET.get('hitsPerPage', 100)
    pages = request.GET.get("page", 0)

    headers = {
        'X-Algolia-Application-Id': ALGOLIA_APP_ID,
        'X-Algolia-API-Key': ALGOLIA_API_KEY
    }
    params = {
        'query': query,
        'filters': filters,
        'facets': facets,
        'page': pages,
        # 'hitsPerPage': hitsperpage
    }
    response_all = requests.get(
        'https://{}.algolia.net/1/indexes/{}'.format(ALGOLIA_APP_ID, LISTING_DATA),
        headers=headers,
        params=params
    )
    results_all = response_all.json()
    rr = results_all['nbPages']
    # print(results_all)

    response_fuel_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA, FUEL),
        headers=headers,
        data=json.dumps({}))
    results_fuel_facet = response_fuel_facet.json()

    response_transmission_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA,
                                                                     TRANSMISSION),
        headers=headers,
        data=json.dumps({}))
    results_transmission_facet = response_transmission_facet.json()

    response_seat_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA, SEATS),
        headers=headers,
        data=json.dumps({}))
    results_seat_facet = response_seat_facet.json()

    response_battery_composition_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA, BATTERY_COMPOSITION),
        headers=headers,
        data=json.dumps({}))
    results_battery_composition_facet = response_battery_composition_facet.json()

    response_charging_port_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA, CHARGING_PORT),
        headers=headers,
        data=json.dumps({}))
    results_charging_port_facet = response_charging_port_facet.json()

    response_charging_type_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA, CHARGING_TYPE),
        headers=headers,
        data=json.dumps({}))
    results_charging_type_facet = response_charging_type_facet.json()

    response_charging_sharing_facet = requests.post(
        'https://{}.algolia.net/1/indexes/{}/facets/{}/query'.format(ALGOLIA_APP_ID, LISTING_DATA, CHARGING_SHARING),
        headers=headers,
        data=json.dumps({}))
    results_charging_sharing_facet = response_charging_sharing_facet.json()

    # print(results_location_facet)
    # print(results_storageType_facet)
    # print(results_building_facet)
    # print(results_unitType_facet)

    context = {
        'data_hits': results_all['hits'],
        'data_all': results_all,
        'data_pagination': results_all['nbPages'],
        'data_fuel_facet': results_fuel_facet['facetHits'],
        'data_transmission_facet': results_transmission_facet['facetHits'],
        'data_seat_facet': results_seat_facet['facetHits'],
        'data_battery_composition_facet': results_battery_composition_facet['facetHits'],
        'data_charging_port_facet': results_charging_port_facet['facetHits'],
        'data_charging_type_facet': results_charging_type_facet['facetHits'],
        'data_charging_sharing_facet': results_charging_sharing_facet['facetHits']
    }
    # print(results_all)
    return render(request, 'listing.html', context)
