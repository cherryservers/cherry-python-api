# -*- coding: utf-8 -*-

import json
import logging
import requests

class MainAPI(object):

    """ Main class for API call """

    def __init__(self, auth_token):

        self.auth_token = auth_token
        self.api_url = "api.cherryservers.com"

    def call_api(self, method, type='GET', args=None):

        api_url = 'https://' + self.api_url + '/' + method

        token_header = 'Bearer ' + self.auth_token

        headers = {
            'Authorization': token_header,
            'Content-Type': 'application/json'
        }

        if type == 'GET':
            resp = requests.get(api_url, headers=headers)
        elif type == 'POST':
            print("URL: %s -> HEADERS: %s -> ARGS: %s" % (api_url, headers, json.dumps(args)))
            resp = requests.post(api_url, headers=headers, data=json.dumps(args))
        elif type == 'DELETE':
            print("delete")
            resp = requests.delete(api_url, headers=headers)
        elif type == 'PUT':
            print("PUT")
            resp = requests.put(api_url, headers=headers, data=json.dumps(args))

        resp.headers.get("content-type", "").startswith("application/json")
        data = resp.json()

        try:
            resp.raise_for_status()
        except requests.HTTPError as e:
            raise Exception("Error detected: %s Details: %s Even more details: %s" % (e, data, json.dumps(args)))

        return data
