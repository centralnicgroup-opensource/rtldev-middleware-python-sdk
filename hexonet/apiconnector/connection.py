from six.moves.urllib.request import urlopen
from six.moves.urllib.parse import urlparse, urlencode
import hexonet.apiconnector.util
from hexonet.apiconnector.response import Response

"""
APICONNECTOR Connection

"""


class Connection:
    def __init__(self, config):
        """
        Constructor
        """
        self._config = config

    def call_raw_http(self, command, config=None):
        """
        Make a curl API call over HTTP(S) and returns the response as a string
        """
        post = {}
        if ('login' in self._config):
            post['s_login'] = self._config['login']
        if ('password' in self._config):
            post['s_pw'] = self._config['password']
        if ('entity' in self._config):
            post['s_entity'] = self._config['entity']
        if ('user' in self._config):
            post['s_user'] = self._config['user']
        if ('role' in self._config):
            post['s_login'] = self._config['login'] + "!" + self._config['role']

        post['s_command'] = hexonet.apiconnector.util.command_encode(command)
        post = urlencode(post)
        response = urlopen(self._config['url'], post.encode('UTF-8'))
        content = response.read()
        return content

    def call_raw(self, command, config=None):
        """
        Make a curl API call and returns the response as a string
        """
        return self.call_raw_http(command, config)

    def call(self, command, config=None):
        """
        Make a curl API call and returns the response as a response object
        """
        return Response(self.call_raw(command, config))
