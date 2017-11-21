# -*- coding: utf-8 -*-

class AuthenticationError(Exception):
    """Invalid authentication credentials.
    """
    pass


class InvalidChecksumError(Exception):
    """MD5 checksum of a local file does not match the one from the server.
    """
    pass


class SentinelAPIError(Exception):
    """Invalid responses from DataHub.
    """

    def __init__(self, msg=None, response=None):
        self.msg = msg
        self.response = response

    def __str__(self):
        return 'HTTP status {0} {1}: {2}'.format(
            self.response.status_code, self.response.reason,
            ('\n' if '\n' in self.msg else '') + self.msg)


class ServerError(Exception):
    """For cases when the server is unreachable, under maintenance, or
    the response is just unparsable garbage.
    """
    pass
