from src.http_common import HttpCommon

# TODO: Move to a better place
# line break and inline space helper variables
l_b = '\n'
l_s = ' '


class HttpResponseBuilder:
    """
    Methods prefixed with in_ where created for internal use, they are not necessarily pure.
    Not for external use
    """

    @staticmethod
    def in_compose(http_request, response_status, response_headers, response_body):
        """
        Build a new http response string
        :param src.http_request.HttpRequest http_request:
        :param response_status:
        :param response_headers:
        :param response_body:
        :return:
        """
        return '{header}{line_break}{body}'.format(
            header=HttpResponseBuilder.in_compose_header(http_request, response_status, response_headers),
            line_break=l_b,
            body=HttpResponseBuilder.in_compose_body(response_body)
        )

    @staticmethod
    def in_compose_header(http_request, response_status, response_headers):
        """
        :param src.http_request.HttpRequest http_request:
        :param dict response_headers:
        :return:
        """
        return '{header_top}{line_break}{header_fields}'.format(
            header_top=HttpResponseBuilder.in_compose_header_first_line(http_request.protocol, response_status),
            line_break=l_b,
            header_fields=HttpResponseBuilder.in_compose_header_fields(response_headers)
        )

    @staticmethod
    def in_compose_body(response_body):
        """
        Validate and sanitize request body
        :param response_body:
        :return:
        """
        return response_body

    @staticmethod
    def in_compose_header_first_line(protocol, response_status):
        """
        Generates first line of response header
        Ex. HTTP/1.1 200 OK
        :param str protocol:
        :param tuple response_status: Status code definition represented as a tuple Ex. (200, OK)
        :return:http_request
        """
        return '{protocol}{space}{status[0]}{space}{status[1]}'.format(
            protocol=protocol,
            space=l_s,
            status=response_status
        )

    @staticmethod
    def in_compose_header_fields(response_headers):
        """
        Generates header fields string based on dict
        If not response header is preset a content type text/plain will be added
        :param dict response_headers:
        :return: Header fields string, with an already added line break at the end IMPORTANT!
        """
        header_fields_string = ''

        if not response_headers or not len(response_headers):
            header_fields_string += HttpCommon.CONTENT_TYPE_TEXT + l_b
        else:
            for field, field_value in response_headers.items():
                header_fields_string += '{}: {}{}'.format(field, field_value, l_b)

        return header_fields_string


# print(HttpResponseBuilder.compose(
#     http_request=HttpRequest('GET', '/', 'HTTP1/1', {}),
#     response_status=HttpCommon.STATUS_OK,
#     response_headers=None,
#     response_body='Hello world'
# ))