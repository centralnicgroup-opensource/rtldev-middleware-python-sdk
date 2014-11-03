import ispapi.util
import urllib, urllib2
from ispapi.response import Response

"""
ISPAPI Connection

"""
class Connection:
	def __init__(self, config):
		"""
		Constructor
		"""
		self._config = config

	def call_raw_http(self, command, config = None):
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

		post['s_command'] = ispapi.util.command_encode(command)

		req = urllib2.Request(self._config['url'], urllib.urlencode(post))
		response = urllib2.urlopen(req)
		content = response.read()
		return content

	def call_raw(self, command, config = None):
		"""
		Make a curl API call and returns the response as a string
		"""
		return self.call_raw_http(command, config)

	def call(self, command, config = None):
		"""
		Make a curl API call and returns the response as a response object
		"""
		return Response(self.call_raw(command, config))


