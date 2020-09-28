from private_vars import api_key
import meraki

API_KEY = api_key

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_638948197133193996'

response = dashboard.appliance.getNetworkApplianceSecurityEvents(
    network_id, total_pages='all'
)

for i in range(len(response)):
    print(response[i])