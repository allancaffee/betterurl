from betterurl import Url

from nose.tools import assert_equal, assert_raises


def test_netloc():
  assert_equal(
    Url(hostname='example.com').netloc,
    'example.com',
  )
  assert_equal(
    Url(username='user', password='password', hostname='example.com').netloc,
    'user:password@example.com',
  )
  assert_equal(
    Url(username='user', hostname='example.com').netloc,
    'user@example.com',
  )
  assert_equal(
    Url(hostname='example.com', port=80).netloc,
    'example.com:80',
  )
  #eq_(
  #  Url(username='username', password='password', hostname='example.com', port=80).netloc,
  #  'username:password@example.com:80',
  #)

def test_netloc_edges():
  # Empty username isn't the same as no username: http://tools.ietf.org/html/rfc1738#section-3.1
  assert_equal(
    Url(username='', hostname='example.com').netloc,
    '@example.com',
  )
  # Empty password isn't the same as no password: http://tools.ietf.org/html/rfc1738#section-3.1
  assert_equal(
    Url(username='user', password='', hostname='example.com').netloc,
    'user:@example.com',
  )
  # TODO: Usernames and passwords must be quoted.
  #assert_equal(
  #  Url(username='user:name', hostname='example.com').netloc,
  #  'user%3Aname@example.com',
  #)

def test_netloc_errors():
  assert_raises(ValueError, getattr, Url(hostname=None), 'netloc')
  assert_raises(ValueError, getattr, Url(password='pass', hostname='example.com'), 'netloc')
