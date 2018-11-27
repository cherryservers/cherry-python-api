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
