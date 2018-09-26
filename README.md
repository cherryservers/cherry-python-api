# README #

Cherry Servers python API for Cherry Servers RESTful API.

### Examples ###

## Get teams
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