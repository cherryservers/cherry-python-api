# -*- coding: utf-8 -*-

from .api import MainAPI


class Master(MainAPI):

    """ Main class for API managament """

    def __init__(self, auth_token, user_agent="", debug=None):

        self.auth_token = auth_token
        self.api_url = "api.cherryservers.com"
        self.user_agent_prefix = user_agent
        self.debug = debug

    def call_api(self, method, type='GET', args=None):

        ''' Cia nustatom pagal nutylejima tipus '''
        return super(Master, self).call_api(method, type, args)

    def get_teams(self, **kwargs):
        """ Get teams ID for further requests
        Link: https://api.cherryservers.com/doc/#operation/get-teams
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/teams', args=args)

    def get_plans(self, team_id, **kwargs):
        """ Get available plans for specified team
        Link: https://api.cherryservers.com/doc/#operation/get-team-plans
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/teams/%s/plans' % team_id, args=args)

    def get_images(self, plan_id, **kwargs):
        """ List supported distributions for specified plan
        Link: https://api.cherryservers.com/doc/#operation/get-plan-images
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/plans/%s/images' % plan_id, args=args)
    
    def get_projects(self, team_id, **kwargs):
        """ Get projects for team
        Link: https://api.cherryservers.com/doc/#operation/get-team-projects
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/teams/%s/projects' % team_id, args=args)

    def get_servers(self, project_id, **kwargs):
        """ Get servers for project
        Link: https://api.cherryservers.com/doc/#operation/get-project-servers
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/servers' % project_id, args=args)
 
    def get_server(self, server_id, **kwargs):
        """ Get single server info
        Link: https://api.cherryservers.com/doc/#operation/get-server
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/servers/%s' % server_id, args=args)

    def create_server(self, project_id, region, plan_id, **kwargs):
        """ Create server in specified project
        Link: https://api.cherryservers.com/doc/#operation/deploy-server
        """

        args = self.update_args(kwargs, {
            "project_id": project_id,
            "region": region,
            "plan_id": plan_id
        })

        return self.call_api('v1/projects/%s/servers'
            % project_id, type='POST', args=args)

    def terminate_server(self, server_id):
        """ Terminated server by ID
        Link: https://api.cherryservers.com/doc/#operation/terminate-server
        """

        return self.call_api('v1/servers/%s' % server_id, type='DELETE')

    def reboot_server(self, server_id):
        """ Reboot server by ID
        Link: https://api.cherryservers.com/doc/#operation/perform-server-action
        """

        args = {
            "type": "reboot"
        }

        return self.call_api('v1/servers/%s/actions'
            % server_id, type='POST', args=args)

    def poweron_server(self, server_id):
        """ Power on server by ID
        Link: https://api.cherryservers.com/doc/#operation/perform-server-action
        """

        args = {
            "type": "power_on"
        }

        return self.call_api('v1/servers/%s/actions'
            % server_id, type='POST', args=args)

    def poweroff_server(self, server_id):
        """ Power off server by ID
        Link: https://api.cherryservers.com/doc/#operation/perform-server-action
        """

        args = {
            "type": "power_off"
        }

        return self.call_api('v1/servers/%s/actions'
            % server_id, type='POST', args=args)

    def get_ssh_keys(self, **kwargs):
        """ List SSH keys
        Link: https://api.stage.cherryservers.com/doc/#operation/get-ssh-keys
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/ssh-keys', args=args)

    def create_ssh_key(self, label, ssh_key):
        """ Adds new ssh key
        Link: https://api.cherryservers.com/doc/#operation/create-ssh-key
        """

        args = {
            "label": label,
            "key": ssh_key
        }

        return self.call_api('v1/ssh-keys', type='POST', args=args)

    def update_ssh_keys(self, ssh_key_id, **kwargs):
        """ Updates ssh key
        Link: https://api.cherryservers.com/doc/#operation/update-ssh-key
        """

        args = self.update_args(kwargs, {})

        return self.call_api('v1/ssh-keys/%s'
            % ssh_key_id, type='PUT', args=args)

    def delete_ssh_key(self, ssh_key_id):
        """ Removes ssh key
        Link: https://api.cherryservers.com/doc/#operation/delete-ssh-key
        """

        return self.call_api('v1/ssh-keys/%s' % ssh_key_id, type='DELETE')

    def get_ip_addresses(self, project_id, **kwargs):
        """ Get all project`s ips available
        Link: https://api.cherryservers.com/doc/#operation/get-ip-addresses
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/ips' % project_id, args=args)

    def get_ip_address(self, project_id, ip_address_id, **kwargs):
        """ Get specific IP
        Link: https://api.cherryservers.com/doc/#operation/get-ip-address
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/ips/%s'
            % (project_id, ip_address_id), args=args)

    def create_ip_address(self, project_id, region, **kwargs):
        """ Orders additional ip address
        Link: https://api.stage.cherryservers.com/doc/#operation/request-ip-address
        """

        args = self.update_args(kwargs, {
            "region": region
        })

        return self.call_api('v1/projects/%s/ips'
            % project_id, type='POST', args=args)

    def update_ip_address(self, project_id, ip_address_id, **kwargs):
        """ Update IP address info
        Link: https://api.stage.cherryservers.com/doc/#operation/update-ip-address
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/ips/%s'
            % (project_id, ip_address_id), type='PUT', args=args)

    def remove_ip_address(self, project_id, ip_address_id):
        """ Removes IP address
        Link: https://api.stage.cherryservers.com/doc/#operation/delete-ip-address
        """

        return self.call_api('v1/projects/%s/ips/%s'
            % (project_id, ip_address_id), type='DELETE')

    def get_ip_subnets(self, project_id, **kwargs):
        """ Get all project`s subnets
        Link: https://api.cherryservers.com/doc/#operation/get-project-subnets
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/subnets' % project_id, args=args)

    def get_ip_subnet(self, project_id, subnet_id, **kwargs):
        """ Get specific IP subnet
        Link: https://api.cherryservers.com/doc/#operation/get-subnet
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/subnets/%s'
            % (project_id, subnet_id), args=args)

    def create_ip_subnet(self, project_id, region, quantity, **kwargs):
        """ Orders additional IP subnet
        Link: https://api.cherryservers.com/doc/#operation/request-subnet
        """

        args = self.update_args(kwargs, {
            "region": region,
            "quantity": quantity
        })

        return self.call_api('v1/projects/%s/subnets'
            % project_id, type='POST', args=args)

    def remove_ip_subnet(self, project_id, subnet_id):
        """ Removes IP subnet
        Link: https://api.cherryservers.com/doc/#operation/delete-subnet
        """

        return self.call_api('v1/projects/%s/subnets/%s'
            % (project_id, subnet_id), type='DELETE')

    def get_storage_volumes(self, project_id, **kwargs):
        """ Get all project`s storage volumes
        Link: https://api.cherryservers.com/doc/#operation/get-project-storages
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/storages' % project_id, args=args)

    def get_storage_volume(self, project_id, storage_id, **kwargs):
        """ Get specific storage volume
        Link: https://api.cherryservers.com/doc/#operation/get-storage
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/storages/%s'
            % (project_id, storage_id), args=args)

    def create_storage_volume(self, project_id, region, size, **kwargs):
        """ Orders storage volume
        Link: https://api.cherryservers.com/doc/#operation/request-storage
        """

        args = self.update_args(kwargs, {
            "region": region,
            "size": size
        })

        return self.call_api('v1/projects/%s/storages'
            % project_id, type='POST', args=args)

    def update_storage_volume(self, project_id, storage_id, **kwargs):
        """ Update storage volume
        Link: https://api.cherryservers.com/doc/#operation/resize-storage
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/storages/%s'
            % (project_id, storage_id), type='PUT', args=args)

    def attach_storage_volume(self, project_id, storage_id, server_id, **kwargs):
        """ Attach storage volume to an existing server
        Link: https://api.cherryservers.com/doc/#operation/attach-storage
        """

        args = self.update_args(kwargs, {
            "attach_to": server_id
        })

        return self.call_api('v1/projects/%s/storages/%s/attachments'
                             % (project_id, storage_id), type='POST', args=args)

    def detach_storage_volume(self, project_id, storage_id, **kwargs):
        """ Detach storage volume from a server
        Link: https://api.cherryservers.com/doc/#operation/deatach-storage
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/storages/%s/attachments'
                             % (project_id, storage_id), type='DELETE', args=args)

    def remove_storage_volume(self, project_id, storage_id):
        """ Removes storage volume from project
        Link: https://api.cherryservers.com/doc/#operation/delete-storage
        """

        return self.call_api('v1/projects/%s/storages/%s'
            % (project_id, storage_id), type='DELETE')

    def get_backup_storage_plans(self, **kwargs):
        """ Get available backup storage plans
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/get-backup-plans
        """
        args = self.update_args(kwargs, {})
        return self.call_api('v1/backup-storage-plans', type='GET', args=args)

    def get_backup_storages(self, project_id, **kwargs):
        """ Get all project`s backup storages
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/get-backup-storages
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/projects/%s/backup-storages' 
            % project_id, args=args)

    def get_backup_storage(self, backup_id, **kwargs):
        """ Get specific backup storage
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/get-backup-storage
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/backup-storages/%s'
            % backup_id, args=args)

    def create_backup_storage_volume(self, server_id, backup_plan, region, **kwargs):
        """ Request backup storage for a server
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/post-backup-storages
        """

        args = self.update_args(kwargs, {
            "slug": backup_plan,
            "region": region
        })

        return self.call_api('v1/servers/%s/backup-storages'
            % server_id, type='POST', args=args)

    def update_backup_storage(self, backup_id, **kwargs):
        """ Update backup storage
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/put-backup
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/backup-storages/%s'
            % backup_id, type='PUT', args=args)

    def remove_backup_storage(self, backup_id):
        """ Removes backup storage from project and server
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/delete-backup-storage
        """

        return self.call_api('v1/backup-storages/%s'
            % backup_id, type='DELETE')

    def update_backup_storage_method(self, backup_id, method_name, **kwargs):
        """ Disable or enable access method and update it's ACL's
        Link: https://api.cherryservers.com/doc/#tag/Backup-Storage/operation/patch-backup-methods
        """

        args = self.update_args(kwargs, {})
        return self.call_api('v1/backup-storages/%s/methods/%s'
            % (backup_id, method_name), type='PATCH', args=args)
