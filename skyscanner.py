import requests
import json

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
key = 'sh428739766321522266746152871799'
query = {
  "query": {
    "market": "UK",
    "locale": "en-GB",
    "currency": "GBP",
    "queryLegs": [
      {
        "originPlaceId": {
          "iata": "LHR",
        #   "entityId": "95565050"
        },
        "destinationPlaceId": {
          "iata": "EDI",
        #   "entityId": "27544008"
        },
        "date": {
          "year": 2023,
          "month": 10,
          "day": 20
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
    "includeSustainabilityData": True,
    "nearbyAirports": True
  }
}


res = requests.post(url,
  headers={
    "x-api-key": key,
    "Content-type": "application/json"
  },
#   json=json.dumps(query)
  json = query
)

print(res.status_code)
# print(res.content)
print(res.json())

'''
curl --location --request POST 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create' \
--header 'x-api-key: sh428739766321522266746152871799' \
--data-raw '...'
'''

