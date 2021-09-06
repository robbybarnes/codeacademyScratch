import meraki
from private_vars import api_key, org_id

dashboard = meraki.DashboardAPI(
    api_key,
    suppress_logging=True,
    print_console=False
)

all_networks = dashboard.organizations.getOrganizationNetworks(org_id)
#print(type(all_networks[0]))

network_id = all_networks[0]["id"]
#print(network_id)

network_devices = dashboard.networks.getNetworkDevices(network_id)

print(network_devices)
