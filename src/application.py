import socket
from src.server import Server
from src.http_handler import HttpHandler


class Application(HttpHandler):
    @property
    def server(self):
        return self._server

    def __init__(self):
        """
        Creates a new instance of Application
        """
        HttpHandler.__init__(self)
        self._server = None
        self._is_running = False

    def listen(self, port):
        """
        Creates a socket, bind it to a given host/port, and start listening
        :param port:
        :return:
        """
        self._server = Server(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((socket.gethostbyname(socket.gethostname()), port))
        self._server.listen(0)
        self._is_running = True
        while True and self._is_running:
            (conn, address) = self._server.accept()
            self.handle_connection(conn, address)