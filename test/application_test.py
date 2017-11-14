import unittest
from src.application import Application


class TestStringMethods(unittest.TestCase):
    def test_server_socket_status(self):
        def get_handler(req):
            print(req)

        app = Application()
        app.get('/gohome', get_handler)
        app.listen(5003)


if __name__ == '__main__':
    unittest.main()