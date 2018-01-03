from builder import HttpResponseBuilder
from ..common.constants import HttpConstants

class HttpResponse:

    def __init__(self, http_request):
        """
        Creates an instance of http response
        :param src.http_request.HttpRequest http_request:
        """
        self._request = http_request

    @classmethod
    def from_request(cls, request):
        """
        Creates a new instance of HttpResponse
        :param request:
        :return:
        """
        return cls(request)

    def json(self, json_data):
        """
        JSON string
        :param str json_data:
        :return:
        """
        response = HttpResponseBuilder.in_compose(
            http_request=self._request,
            response_status=HttpConstants.STATUS_OK,
            response_body=json_data,
            response_headers={
                'Content-Type': 'application/json',
                'Content-Length': len(json_data.encode('utf-8'))
            }
        )
        self._request.connection.send(response.encode('utf-8'))