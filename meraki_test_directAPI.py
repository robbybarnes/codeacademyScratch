import requests
import meraki
import json
from private_vars import api_key, org_id

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
  # print(f"The Organization {name}'s ID is {id}")

# Write the org_id_dict dictionary to a JSON file
# with open('org_id.json','w') as f:
#     json.dump(org_id_dict, f, indent=2)


#Get the individual networks from each org ID

networks = requests.request("GET",f"{url}/organizations/{org_id}/networks",headers=headers,data=payload).json()

for network in networks:
    name = network['name']
    id = network['id']
    print(f"Network {name} has an ID of {id}")


# Write the response in to a JSON file in the current directory
# with open('response.json','w') as f:
#     json.dump(response, f, indent=2)

#while loop for the same thing but it will also give the index number of each item
# index = 0
# while index < len(response):
#   print(f"The organization with the index of {index} is {response[index]}")
#   index +=1


#print the number of items in the list that is returned
# print(len(response))
