"""A better URL manipulation library."""
import urlparse


class Url(object):

  def __init__(self, scheme=None, username=None, password=None, hostname=None, port=None, path=None, params=None, fragment=None):
    self.scheme = scheme
    self.username = username
    self.password = password
    self.hostname = hostname
    self.port = port
    self.path = path
    self.params = params
    self.fragment = fragment

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

  @property
  def __user_pass(self):
    # TODO: Escape the username and password (using urllib.quote?).
    if self.username is None and self.password is not None:
      raise ValueError('Password cannot exist without username. [RFC-1738]')
    if None not in (self.username, self.password):
      return '{0}:{1}'.format(self.username, self.password)
    elif self.username is not None:
      return self.username
