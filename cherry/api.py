# -*- coding: utf-8 -*-

import json
import requests
from . import __version__

class MainAPI(object):

    """ Main class for API call """

    def __init__(self, auth_token, user_agent="", debug=None):

        self.auth_token = auth_token
        self.api_url = "api.cherryservers.com"
        self.user_agent_prefix = user_agent
        self.debug_cherry = debug

    def call_api(self, method, type='GET', args=None):

        api_url = 'https://' + self.api_url + '/' + method
        token_header = 'Bearer ' + self.auth_token
        agent = "{0}cherry-python/{1} {2}/{3}".format(self.user_agent_prefix,
                                         __version__,
                                         requests.__name__,
                                         requests.__version__)

        headers = {
            'Authorization': token_header,
            'Content-Type': 'application/json',
            'User-Agent': agent
        }

        if self.debug:
            print('Request data:')
            print(json.dumps(args, indent=2))

        if type == 'GET':
            api_url += self._parse_params(args)
            resp = requests.get(api_url, headers=headers)
        elif type == 'POST':
            resp = requests.post(api_url, headers=headers, data=json.dumps(args))
        elif type == 'DELETE':
            resp = requests.delete(api_url, headers=headers)
        elif type == 'PUT':
            resp = requests.put(api_url, headers=headers, data=json.dumps(args))

        if not resp.content:
            data = None
        elif resp.headers.get("content-type", "").startswith("application/json"):
            try:
                data = resp.json()
            except Exception as e:
                raise Exception("Failed to read json data: %s" % e)
        else:
            data = resp.content

        try:
            if resp.status_code != 404 and resp.status_code != 400:
                resp.raise_for_status()
        except requests.HTTPError as e:
            raise Exception("Error detected: %s Details: %s More details: %s"
                % (e, data, json.dumps(args)))

        return data

    def update_args(self, args, updates):
        args = args.copy() if isinstance(args, dict) else json.dumps(args)
        args.update(updates)
        return args

    def _parse_params(self, params):
        vals = list()
        for k, v in params.items():
            vals.append(str("%s=%s" % (k, v)))
        return "?" + "&".join(vals)