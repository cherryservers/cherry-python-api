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

plans = master.get_plans("28519")

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

images = master.get_images("161")

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

projects = master.get_projects("28519")

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

servers = master.get_servers("79813")

for server in servers:
    sr = json.dumps(server)
    parse_sr = json.loads(sr)

    print("Server ID: %s -> IP: %s" % (parse_sr['id'], parse_sr['ip_addresses']))
```

### Get specific server info 
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

server = master.get_server("165903")

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
                              region="EU-East-1",
                              ip_addresses=ips,
                              ssh_keys=ssh_keys,
                              plan_id="161")

print("Server: %s" % server)
```

#### Terminate server
```
import cherry
import json

master = cherry.Master(auth_token="api_token")

server = master.terminate_server("165760")
print("Delete server: %s" % server)
```