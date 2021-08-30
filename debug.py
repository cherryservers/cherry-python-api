# -*- coding: utf-8 -*-
import cherry
import json

master = cherry.Master(auth_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJjIjoyMDkwNSwiaSI6IiIsInIiOiJyY2YiLCJ0IjoidWMiLCJhIjowLCJpYXQiOjE2MTcwODY3Nzl9.dMVYLZbr_RzuzR7ZokFtcL7_mKaWUiAF1d8JjFmqw8Xc_8eufwom8dssAwLZ_8d8HFfj_oSsRLVeGA14InFGJ7S3CmM6ovoH7qOhAvoUhTJod76DUpqfFOLgEazUHVJAnX2-C48LU31b5IMNyjuD-W5V8hXBR1H2pZFY809qUkcb6-nHyBmmdc1Z9mpNG2jEGowC2z2biB6BLVOaEtal90N_XZas1D5ItlKwDUErPgT602xFQhYZG9a0cPsMsIPB1ONkb4thVBm76-7Pp55syZrOfYMv5mnSCF-H0ksmbBjNvqznaTlvH-WWQg2uYDtZUDWuOnZZTjPu6IdpgKrpCg",
user_agent="ansible-module-")
teams = master.get_projects(team_id=15592)

for team in teams:
    t = json.dumps(team)
    parse_t = json.loads(t)
    print("Team ID: %s -> Team Name: %s" % (parse_t['id'], parse_t['name']))

