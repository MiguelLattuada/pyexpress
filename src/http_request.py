class HttpRequest:

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
