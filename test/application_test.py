import unittest
from src.application import Application


class TestStringMethods(unittest.TestCase):
    def test_server_socket_status(self):
        def get_handler(req, res):
            """
            GET handler
            :param src.http_request.HttpRequest req:
            :param src.http_response.HttpResponse res:
            :return:
            """
            res.json('{ "standard": "json", "format": "from", "python": 3 }')

        app = Application()
        app.get('/', get_handler)
        app.listen(5003)


if __name__ == '__main__':
    unittest.main()