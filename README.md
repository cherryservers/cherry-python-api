# README #

Cherry Servers python API for Cherry Servers RESTful API.

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
    print("Plan id: %s -> Plan name: %s -> Av: %s" % (parse_p['id'], parse_p['name'], parse_p['available_regions']))
```

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact