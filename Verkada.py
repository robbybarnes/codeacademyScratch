import requests
org_id = "9c976e6a-4fa3-4be3-ad5e-d5d258c16cfb"
api_key = "MsNlDBwNnP9RhdlLTEC0X2pLyo5O6wuQ23LaKAM1"

url = f"https://api.verkada.com/orgs/{org_id}/notifications"

querystring = {"notification_type":"camera_online","per_page":"100","include_image_url":"false"}

headers = {
    "Accept": "application/json",
    "x-api-key": api_key
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)