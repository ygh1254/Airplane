import requests
import json

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
key = 'sh428739766321522266746152871799'
query = {
  "query": {
    "market": "KR",
    "locale": "en-GB",
    "currency": "KRW",
    "queryLegs": [
      {
        "originPlaceId": {
          "iata": "ICN",
        #   "entityId": "95565050"
        },
        "destinationPlaceId": {
          "iata": "CTS",
        #   "entityId": "27544008"
        },
        "date": {
          "year": 2023,
          "month": 12,
          "day": 23
        }
      }
    ],
    "cabinClass": "CABIN_CLASS_ECONOMY",
    "adults": 1,
    # "childrenAges": [0],
    # "includedCarriersIds": ["BA"],
    # "excludedCarriersIds": ["U2"],
    # "includedAgentsIds": ["BA"],
    # "excludedAgentsIds": ["U2"],
    # "includeSustainabilityData": True,
    # "nearbyAirports": True
  }
}


res = requests.post(url,
  headers={
    "x-api-key": key,
    "Content-type": "application/json"
  },
  json = query
)

print(res.status_code)
data = res.json()
'''
data
sessionToken : Session token that is used to poll.
status
    RESULT_STATUS_UNSPECIFIED: Results status not specified.
    RESULT_STATUS_COMPLETE: Results are now complete.
    RESULT_STATUS_INCOMPLETE: Results are not complete yet.
    RESULT_STATUS_FAILED: Search has failed.
action
    RESULT_ACTION_UNSPECIFIED: Result action is not specified.
    RESULT_ACTION_REPLACED: Result action is to replace, as the results have been changed.
    RESULT_ACTION_NOT_MODIFIED: Result action is not to modify, as no changes have occurred.
    RESULT_ACTION_OMITTED: Results for this vertical have been omitted.
content
    results : Search results object.
        itineraries
            property name
                price
                    amount : int64 price value amount serialised as a string. It could be an empty string if the value is missing.
                    unit
                        PRICE_UNIT_WHOLE: unit relation: 1. eg: A whole pound, euro, etc.
                        PRICE_UNIT_CENTI: unit relation: 100; eg: cents
                        PRICE_UNIT_MILLI: unit relation: 1000
                        PRICE_UNIT_MICRO: unit relation: 1000000
                    updateStatus
                        PRICE_UPDATE_STATUS_UNSPECIFIED: The update status is not set.
                        PRICE_UPDATE_STATUS_PENDING: The price is still updating.
                        PRICE_UPDATE_STATUS_CURRENT: The price is current.
    stats : Stats object.
    sortingOptions : Sorting options object contains data for sorting by best, cheapest or fastest criteria.
'''
# print(data['sessionToken'])
# print(data['status'])
# print(data['action'])
# print(data['content'])
# print(data['content']['results'])
# print(data['content']['results']['itineraries'])
for element in data['content']['results']['itineraries'] :
    print(element)
    print(data['content']['results']['itineraries'][element]['pricingOptions'])
    print(data['content']['results']['itineraries'][element]['pricingOptions'][0])
    print()
# print(data['content']['results']['legs'])
# print(data['content']['stats'])
# print(data['content']['sortingOptions'])


