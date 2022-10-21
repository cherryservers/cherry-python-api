# README #

Cherry Servers python API for Cherry Servers RESTful API.

Installation
------------
The Cherry Servers api python lybrary should be installed by pip:

````
pip install cherry-python
````

### Examples ###

#### Get teams
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

teams = master.get_teams()

for team in teams:
    t = json.dumps(team)
    parse_t = json.loads(t)
    print("Team ID: %s -> Team Name: %s" % (parse_t['id'], parse_t['name']))
```

#### Get plans
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

plans = master.get_plans(team_id="28519")

for plan in plans:
    p = json.dumps(plan)
    parse_p = json.loads(p)
    print("Plan id: %s -> Plan name: %s -> Av: %s" % (parse_p['id'], 
                                                      parse_p['name'], 
                                                      parse_p['available_regions']))
```

#### Get only bare metal plans
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

plans = master.get_plans(team_id="28519", **{'type[]':'baremetal'})

for plan in plans:
    p = json.dumps(plan)
    parse_p = json.loads(p)
    print("Plan id: %s -> Plan name: %s -> Av: %s" % (parse_p['id'], 
                                                      parse_p['name'], 
                                                      parse_p['available_regions']))
```

#### Get images
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

images = master.get_images(plan_id="161")

for image in images:
    i = json.dumps(image)
    parse_i = json.loads(i)

    print("Image ID: %s -> Image Name: %s" % (parse_i['id'], 
                                              parse_i['name']))
```

#### Get projects
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

projects = master.get_projects(team_id="28519")

for project in projects:
    p = json.dumps(project)
    parse_p = json.loads(p)

    print("Project ID: %s -> Project name: %s" % (parse_p['id'], 
                                                  parse_p['name']))
```

#### Get SSH keys
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

keys = master.get_ssh_keys()

for key in keys:
    print("Key: %s" % key)
```

#### Get installed servers
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

servers = master.get_servers(project_id="79813")

for server in servers:
    sr = json.dumps(server)
    parse_sr = json.loads(sr)

    print("Server ID: %s -> IP: %s" % (parse_sr['id'], parse_sr['ip_addresses']))
```

#### Get server info 
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

server = master.get_server(server_id="165903")

print(server)
```

#### Get specific server info
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

server = master.get_server(server_id="165903", fields="power,state,termination_date")

print(server)
```

#### Order server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

ips = []
ssh_keys=['95']

server = master.create_server(project_id="79813", 
                              name="super-duper",
                              hostname="bla.com",
                              image="Ubuntu 16.04 64bit", 
                              region="EU-Nord-1",
                              ip_addresses=ips,
                              ssh_keys=ssh_keys,
                              plan_id="161")

print("Server: %s" % server)
```

#### Order first available server from spot market 
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
plans = master.get_plans(team_id="28519", fields="id,name,available_regions,region")

for plan in plans:
    for region in plan['available_regions']:
        if region['spot_qty'] > 0:
            server = master.create_server(project_id="79813",
                                          region=region['name'],
                                          plan_id=plan['id'],
                                          spot_market="1")
            print("%s server (ID %s) deployment has just been started from spot market" % (plan['name'], server['id']))
            exit()
print("No available servers in spot market")
```

#### Terminate server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
server = master.terminate_server(server_id="165760")

print("Delete server: %s" % server)
```

#### Order IP subnet
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
subnet = master.create_ip_subnet(project_id="46776",
                                 quantity="8",
                                 region="EU-Nord-1")
print("Subnet: %s" % subnet)
```

#### Assign subnet IP addresses to a server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
subnet = master.get_ip_subnet(project_id=46776, subnet_id="377432", fields="subnet,id")
server_id = "377441"

for subnet_ip in subnet["addresses"]:
    master.update_ip_address(project_id=46776, ip_address_id=subnet_ip["id"], assigned_to=server_id)
    
    print("Subnet IP %s assigned to a server %s" % (subnet_ip, server_id))
```

#### Remove subnet IP addresses from a server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
subnet = master.get_ip_subnet(project_id=46776, subnet_id="377432", fields="subnet,id,assigned_to")

for subnet_ip in subnet["addresses"]:
    if subnet_ip["assigned_to"]:
        master.update_ip_address(project_id=46776, ip_address_id=subnet_ip["id"], assigned_to="")
        print("Subnet IP %s removed from a server %s" % (subnet_ip["id"], subnet_ip["assigned_to"]["id"]))
```

#### Order storage volume
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
size_in_gb = 100
storage = master.create_storage_volume(project_id=46776, region="EU-Nord-1", size=size_in_gb)

print("Storage: %s" % storage)
```

#### Attach storage volume to a server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
storage = master.attach_storage_volume(project_id=46776, storage_id=377447, server_id="377441")

print("Storage attached to: %s" % storage["attached_to"]["href"])
```

#### Detach storage volume from a server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
storage = master.detach_storage_volume(project_id=46776, storage_id=377447)

print("Storage detached")
```
#### Increase storage volume size
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
size_in_gb = 200
storage = master.update_storage_volume(project_id=46776, storage_id=377457, size=size_in_gb)

print("Storage size upgraded")
```

#### Get backup plans
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
plans = master.get_backup_storage_plans()

for plan in plans:
    p = json.dumps(plan)
    parse_p = json.loads(p)
    print("Plan slug: %s -> Plan size: %s GB -> Available regions: %s" % (parse_p['slug'], 
                                                      parse_p['size_gigabytes'], 
                                                      ' '.join([i['slug'] for i in parse_p['regions']])))
```

#### Request backup storage for a server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")
backup = master.create_backup_storage_volume(server_id=112223344, backup_plan="backup_100", region="eu_nord_1")

print("Backup: %s" % backup)
```