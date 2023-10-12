import requests
import datetime
import json
from pytimekr import pytimekr

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
key = 'sh428739766321522266746152871799'

year = 2023
month = 12
day = 25

query = {
  "query": {
    "market": "KR",
    # Change 'locale' to Korea
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
          "year": year,
          "month": month,
          "day": day
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

# print(res.status_code)
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
if datetime.date(year, month, day) in pytimekr.holidays(year=year):
    print('holiday!', datetime.date(year, month, day))
print(f'Following is result of {datetime.date(year, month, day)} {datetime.date(year, month, day).strftime("%A")}')
print()

# print(data['content']['results']['carriers'])

for index in data['content']['results']['itineraries'] :
    print(index)
    # 12409-2312232030--31964-2-10783-2312250745 -> -31964 : 항공사(carriers)
    for element in data['content']['results']['itineraries'][index]['pricingOptions'] :
        unit = element['price']['unit'] # 가격 단위
        amount = element['price']['amount'] # 가격
        # print('stats')
        # print(data['content']['stats'])
        # agent : 예약사 -> 같은 비행기라도 예약사에 따라 가격이 다른데 어떻게 처리할 것인지? 최소값? 항공사=예약사?
        # agent = element['agentIds']
        # print(agent)
        if amount == '' :
            # print(element)
            pass
        elif unit == 'PRICE_UNIT_WHOLE':
            print(float(amount))
        elif unit == 'PRICE_UNIT_CENTI':
            print(float(amount) / 100)
        elif unit == 'PRICE_UNIT_MILLI':
            print(float(amount) / 1000)
        else :
            print(float(amount) / 1000000)
    print()

