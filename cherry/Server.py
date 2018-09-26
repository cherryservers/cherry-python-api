# -*- coding: utf-8 -*-


class Server():

    """ Class for Server actions """

    def __init__(self, data, master):
        self.master = master

    def reboot(self, server_id, args=None):

        server = self.master.call_api('v1/servers/%s/actions' % server_id, type='POST', args=args)
        return server