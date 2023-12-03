import requests
import os

api_key = ""
try:
    with open(
        os.path.join(
            os.path.dirname(__file__), "keys", "journey-maps-api-sbb.txt"
        ),
        "r",
    ) as file:
        api_key = file.read()
except Exception as e:
    print(e)

path = "/v1/route"
url = "https://journey-maps.api.sbb.ch" + path
params = {"fromStationID": 8503000, "toStationID": 8509000, "api_key": api_key}

response = requests.get(url, params=params)
# print(response.json())

########################################################

try:
    with open(
        os.path.join(
            os.path.dirname(__file__), "keys", "journey-maps-tiles-api-sbb.txt"
        ),
        "r",
    ) as file:
        api_key = file.read()
except Exception as e:
    print(e)

path = "/styles.json"
url = "https://journey-maps-tiles.api.sbb.ch" + path
params = {"api_key": api_key}

response = requests.get(url, params=params)
# print(response.json())

########################################################################

client_secret = ""
try:
    with open(
        os.path.join(
            os.path.dirname(__file__), "keys", "microsoft_key.txt"
        ),
        "r",
    ) as file:
        client_secret = file.read()
except Exception as e:
    print(e)
token_url = "https://login.microsoftonline.com/2cda5d11-f0ac-46b3-967d-af1b2e1bd01a/oauth2/v2.0/token"
token_data = {
    "grant_type": "client_credentials",
    "scope": "api://c11fa6b1-edab-4554-a43d-8ab71b016325/.default",
    "client_id": "f132a280-1571-4137-86d7-201641098ce8",
    "client_secret": client_secret,
}
token_response = requests.post(token_url, data=token_data)
token = token_response.json()["access_token"]

path = "/v3/trips/by-origin-destination"
url = "https://journey-service-int.api.sbb.ch" + path
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
json = {
    "origin": "8503000",
    "destination": "8507000",
    "date": "2023-04-18",
    "time": "13:07",
    "includeAccessibility": "ALL",
}
response = requests.post(url=url, headers=headers, json=json)
print(response.status_code)

path = "/v3/INCUBATOR/trips/by-road"
url = "https://journey-service-int.api.sbb.ch" + path
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
params = {
    "origin": "8503000",
    "destination": "8507000",
}
response = requests.get(url=url, headers=headers, params=params)
print(response.text)

#######################################################################

url = "https://data.sbb.ch/api/explore/v2.1/catalog/datasets/mobilitat/records"
params = {
    "limit": 1,
    "refine": 'parkrail_preis_tag:"0.0"',
    "refine": 'bezeichnung_offiziell:"Linthal"',
}

response = requests.get(url, params=params)
# print(response.json())
