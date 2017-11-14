class HttpRequest:

    @property
    def base_url(self):
        """
        The URL path matched
        :return:
        """
        return self.resource

    @property
    def body(self):
        return None

    @property
    def cookies(self):
        return None

    @property
    def hostname(self):
        """
        Contains the hostname derived from the Host HTTP header.
        :return:
        """
        return self._hostname

    def __init__(self, method, resource, protocol, header_fields):
        """
        Create a new instance of HttpRequest
        :param str method:
        :param str resource:
        :param str protocol:
        :param dict header_fields:
        """
        self.method = method
        self.resource = resource
        self.protocol = protocol
        self.header_fields = header_fields
        (self._hostname, self._port) = self.decouple_host_header()

    def decouple_host_header(self):
        """
        Parse host header field
        :return:
        """
        # TODO: Move helper methods to a separate class
        return tuple(self.header_fields.get('host').split(':'))