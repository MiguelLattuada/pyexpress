from src.http_request import HttpRequest


class HttpRequestParser:

    @staticmethod
    def parse(connection_request):
        """
        Parse incoming connection string
        :param bytes connection_request:
        :return:
        """
        _connection_request = str(connection_request, encoding='utf-8')
        _header_fields = dict()
        _method = None
        _resource = None
        _protocol = None
        lines = _connection_request.split('\r\n')
        request_line = lines[0]
        header_fields = lines[1:]
        (_method, _resource, _protocol) = tuple(request_line.split(' '))

        for field in header_fields:
            parsed_field = field.split(':', 1)
            if len(parsed_field) > 1:
                field_key = parsed_field[0]
                field_value = parsed_field[1][1:]
                _header_fields[field_key.lower()] = field_value

        return HttpRequest(_method, _resource, _protocol, _header_fields)
