import requests
import meraki
import json
from private_vars import api_key, org_id

class Meraki_Organization():
    pass


url = "https://api.meraki.com/api/v1"
dashboard = meraki.DashboardAPI(
  api_key,
  )

payload = {}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

response = requests.request("GET",
                            f"{url}/organizations",
                            headers=headers,
                            data=payload
                            ).json()

org_id_dict = dict()
network_id_dict = dict()

#Iterate over each item in the response and print it separately
for i in response:
  name = i['name']
  id = i['id']
  org_id_dict[name] = id
  #print(f"The Organization {name}'s ID is {id}")

meraki_org = Meraki_Organization()

for key, value in org_id_dict.items():
    setattr(meraki_org, key, value)

print(meraki_org.Sidewinders)