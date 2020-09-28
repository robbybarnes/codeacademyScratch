import meraki
from private_vars import api_key, org_id

dashboard = meraki.DashboardAPI(
    api_key,
    suppress_logging=True,
    print_console=False
)

all_networks = dashboard.organizations.getOrganizationNetworks(org_id)
print(all_networks)

