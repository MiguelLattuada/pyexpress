
class HttpRequest:

    @property
    def base_url(self):
        """
        The URL path matched
        :return:
        """
        return self._resource

    @property
    def hostname(self):
        """
        Contains the hostname derived from the Host HTTP header.
        :return:
        """
        return self._hostname

    @property
    def method(self):
        """
        Contains a string corresponding to the HTTP method of the request: GET, POST, PUT, and so on.
        :return:
        """
        return self._method

    @property
    def protocol(self):
        """
        Contains the request protocol string
        :returns:
        """
        return self._protocol

    @property
    def connection(self):
        """
        Returns http request related socket
        :return:
        """
        return self._connection

    def __init__(self, method, resource, protocol, header_fields):
        """
        Create a new instance of HttpRequest
        :param str method:
        :param str resource:
        :param str protocol:
        :param dict header_fields:
        """
        self._method = method
        self._resource = resource
        self._protocol = protocol
        self._header_fields = header_fields
        (self._hostname, self._port) = self.decouple_host_header()
        self.set_connection(None)

    @classmethod
    def from_incoming_data(cls, incoming_data):
        """
        Creates a new instance of HttpRequest based on incoming data
        :param incoming_data:
        :return:
        """
        from src.http_request_parser import HttpRequestParser
        return HttpRequestParser.parse(incoming_data)

    def decouple_host_header(self):
        """
        Parse host header field
        :return:
        """
        # TODO: Move helper methods to a separate class
        return tuple(self._header_fields.get('host').split(':')) if self._header_fields.get('host') else ('', '')

    def set_connection(self, connection):
        """
        Set socket connection
        :param socket.socket | None connection:
        :return:
        """
        self._connection = connection
