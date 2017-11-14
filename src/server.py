import socket


class Server(socket.socket):

    def __init__(self, family, type):
        """
        Create a new instance of server (which is a wrapper for socket.socket running)
        :param socket.socket socket:
        """
        socket.socket.__init__(
            self,
            family=family,
            type=type
        )