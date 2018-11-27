# -*- coding: utf-8 -*-

from .api import MainAPI


class Master(MainAPI):

    """ Main class for API managament """

    def __init__(self, auth_token):

        self.auth_token = auth_token
        self.api_url = "api.cherryservers.com"

    def call_api(self, method, type='GET', args=None):

        ''' Cia nustatom pagal nutylejima tipus '''
        return super(Master, self).call_api(method, type, args)

    def get_teams(self, args={}):

        """ Get teams ID for further requests """

        cmd = self.call_api('v1/teams', args=args)
        return cmd

    def get_plans(self, team_id):

        """ Get available plans for specified team """

        plans = self.call_api('v1/teams/%s/plans' % team_id)
        return plans

    def get_images(self, plan_id):

        """ List supported distributions for specified plan """

        images = self.call_api('v1/plans/%s/images' % plan_id)
        return images
    
    def get_projects(self, team_id):

        """ Get projects for team """

        projects = self.call_api('v1/teams/%s/projects' % team_id)
        return projects

    def get_servers(self, project_id):

        """ Get servers for project """

        servers = self.call_api('v1/projects/%s/servers' % project_id)
        return servers
 
    def get_server(self, server_id):

        """ Get single server info """

        server = self.call_api('v1/servers/%s' % server_id)
        return server

    def create_server(self, 
                      project_id, 
                      hostname, 
                      image, 
                      region, 
                      ip_addresses, 
                      ssh_keys, 
                      plan_id):

        """ Create server in specified project """

        args = {
            "project_id" : project_id,
            "hostname" : hostname,
            "image" : image,
            "region" : region,
            "ip_addresses" : ip_addresses,
            "ssh_keys" : ssh_keys,
            "plan_id" : plan_id
        }

        server = self.call_api('v1/projects/%s/servers' 
            % project_id, type='POST', args=args)
        return server

    def terminate_server(self, server_id):

        """ Terminated server by ID """

        server = self.call_api('v1/servers/%s' % server_id, type='DELETE')
        return server

    def reboot_server(self, server_id):

        """ Reboot server by ID """

        args = {
            "type" : "reboot"
        }

        server = self.call_api('v1/servers/%s/actions' 
            % server_id, type='POST', args=args)
        return server

    def poweron_server(self, server_id):

        """ Power on server by ID """

        args = {
            "type" : "power_on"
        }

        server = self.call_api('v1/servers/%s/actions' 
            % server_id, type='POST', args=args)
        return server

    def poweroff_server(self, server_id):

        """ Power off server by ID """

        args = {
            "type" : "power_off"
        }

        server = self.call_api('v1/servers/%s/actions' 
            % server_id, type='POST', args=args)
        return server

    def get_ssh_keys(self):

        """ List SSH keys """

        ssh_keys = self.call_api('v1/ssh-keys')
        return ssh_keys

    def create_ssh_key(self, label, ssh_key):

        """ Adds new ssh key """

        args = {
            "label" : label,
            "key" : ssh_key
        }

        key = self.call_api('v1/ssh-keys', type='POST', args=args)
        return key

    def update_ssh_keys(self, ssh_key_id, label, ssh_key):

        """ Updates ssh key """

        args = {
            "label" : label,
            "key" : ssh_key
        }

        key = self.call_api('v1/ssh-keys/%s' 
            % ssh_key_id, type='PUT', args=args)
        return key

    def delete_ssh_key(self, ssh_key_id):

        """ Removes ssh key """

        key = self.call_api('v1/ssh-keys/%s' % ssh_key_id, type='DELETE')
        return key

    def get_ip_addresses(self, project_id):

        """ Get all project`s ips available """

        ips = self.call_api('v1/projects/%s/ips' % project_id)
        return ips

    def get_ip_address(self, project_id, ip_address_id):

        """ Get specific IP """

        ip = self.call_api('v1/projects/%s/ips/%s' 
            % (project_id, ip_address_id))
        return ip

    def create_ip_address(self, 
                          project_id,
                          ip_type,
                          region, 
                          ptr_record, 
                          a_record, 
                          routed_to, 
                          assigned_to):

        """ Orders additional ip address """

        args = {
            "type" : ip_type,
            "region" : region,
            "ptr_record" : ptr_record,
            "a_record" : a_record,
            "routed_to" : routed_to,
            "assigned_to" : assigned_to
        }

        ip = self.call_api('v1/projects/%s/ips' 
            % project_id, type='POST', args=args)
        return ip

    def update_ip_address(self, 
                          project_id, 
                          ip_address_id, 
                          ptr_record, 
                          a_record, 
                          routed_to, 
                          assigned_to):

        """ Update IP address info """

        args = {
            "ptr_record" : ptr_record,
            "a_record" : a_record,
            "routed_to" : routed_to,
            "assigned_to" : assigned_to
        }

        ip = self.call_api('v1/projects/%s/ips/%s' 
            % (project_id, ip_address_id), type='PUT', args=args)
        return ip

    def remove_ip_address(self, project_id, ip_address_id):

        """
        Removes IP address
        """

        ip = self.call_api('v1/projects/%s/ips/%s' 
            % (project_id, ip_address_id), type='DELETE')
        return ip