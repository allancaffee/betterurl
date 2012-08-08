"""A better URL manipulation library."""
import urlparse


class Url(object):

  def __init__(self, scheme=None, username=None, password=None, hostname=None, port=None, path=None, params=None, fragment=None, query=None):
    self.scheme = scheme
    self.username = username
    self.password = password
    self.hostname = hostname
    self.port = port
    self.path = path
    self.params = params
    self.fragment = fragment
    self.query = query

  @property
  def netloc(self):
    """The netloc as described by RFC 1738.

    Refer to http://tools.ietf.org/html/rfc1738

    """
    if self.hostname is None:
      raise ValueError('netloc is not valid without a hostname.')
    netloc = self.hostname
    user_pass = self.__user_pass
    if user_pass is not None:
      netloc = '{0}@{1}'.format(user_pass, netloc)
    if self.port is not None:
      netloc = '{0}:{1}'.format(netloc, self.port)
    return netloc

  @netloc.setter
  def netloc(self, netloc):
    if not netloc.startswith('//'):
      netloc = '//{0}'.format(netloc)
    url = urlparse.urlparse(netloc)
    self.hostname = url.hostname
    self.username = url.username
    self.password = url.password
    self.port = url.port

  @property
  def __user_pass(self):
    # TODO: Escape the username and password (using urllib.quote?).
    if self.username is None and self.password is not None:
      raise ValueError('Password cannot exist without username. [RFC-1738]')
    if None not in (self.username, self.password):
      return '{0}:{1}'.format(self.username, self.password)
    elif self.username is not None:
      return self.username

  def __str__(self):
    url = urlparse.ParseResult(
      scheme=self.scheme,
      netloc=self.netloc,
      path=self.path,
      params=self.params,
      query=self.query,
      fragment=self.fragment,
    )
    return urlparse.urlunparse(url)

  @classmethod
  def from_string(cls, url):
    url = urlparse.urlparse(url)
    return cls(
      scheme=url.scheme,
      username=url.username,
      password=url.password,
      hostname=url.hostname,
      port=url.port,
      path=url.path,
      params=url.params,
      query=url.query,
      fragment=url.fragment,
    )

  def __eq__(self, other):
    if not isinstance(other, Url):
      return False
    return str(self) == str(other)

  def __repr__(self):
    return str(self)
