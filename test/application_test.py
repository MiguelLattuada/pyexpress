import unittest
from src.application import Application


class TestStringMethods(unittest.TestCase):
    def test_server_socket_status(self):
        def get_handler(req):
            """
            GET handler
            :param src.http_request.HttpRequest req:
            :return:
            """
            print(req.hostname)

        app = Application()
        app.get('/gohome', get_handler)
        app.listen(5003)


if __name__ == '__main__':
    unittest.main()