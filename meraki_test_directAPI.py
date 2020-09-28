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
  'Accept': 'application/json',
  'X-Cisco-Meraki-API-Key': api_key
}

response = requests.request("GET", f"{url}/organizations", headers=headers, data=payload).json()

#Iterate over each item in the response and print it separately
# for i in response:
#   print(i)

#while loop for the same thing but it will also give the index number of each item
index = 0
while index < len(response):
  print(f"The organization with the index of {index} is {response[index]}")
  index +=1


#print the number of items in the list that is returned
# print(len(response))
