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
        :return:
        """
        return self._protocol

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

    def decouple_host_header(self):
        """
        Parse host header field
        :return:
        """
        # TODO: Move helper methods to a separate class
        return tuple(self._header_fields.get('host').split(':'))