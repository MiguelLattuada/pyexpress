from socket import socket
from src.http_request_parser import HttpRequestParser


class HttpHandler:

    def __init__(self):
        self._registry = dict()
        pass

    def get(self, resource, callback_action):
        """
        Add a new GET handler to the registry
        :param str resource:
        :param function callback_action:
        :return:
        """
        self.register_handler('GET', resource, callback_action)

    def register_handler(self, method, resource, callback):
        """
        Add a new handler to the registry
        :param str method:
        :param str resource:
        :param function callback:
        :return:
        """
        self._registry[HttpHandler.name_constructor(method, resource)] = callback

    def handle_connection(self, connection, address):
        """
        Handle incoming connection
        :param socket connection:
        :param (str, str) address:
        :return:
        """
        incoming_connection_data = connection.recv(1024)
        http_request = HttpRequestParser.parse(incoming_connection_data)
        handler = self.match_handler(http_request)
        if handler:
            handler(http_request)
            connection.close()

    def match_handler(self, http_request):
        """
        Match the incoming request with a given handler
        :param src.http_request.HttpRequest http_request:
        :return:
        """
        registry_entry_name = HttpHandler.name_constructor(http_request.method, http_request.base_url)
        handler = self._registry.get(registry_entry_name)
        return handler

    @staticmethod
    def name_constructor(method, resource):
        """
        Creates name convention for handlers
        :param str method:
        :param str resource:
        :return:
        """
        return '{}/{}'.format(method, resource)
