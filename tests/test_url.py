from betterurl import Url

from nose.tools import assert_equal, assert_raises


def test_netloc():
  assert_equal(
    Url(hostname='example.com').netloc,
    'example.com',
  )
  assert_equal(
    Url(username='user', hostname='example.com').netloc,
    'user@example.com',
  )
  assert_equal(
    Url(username='user', password='password', hostname='example.com').netloc,
    'user:password@example.com',
  )
  assert_equal(
    Url(hostname='example.com', port=80).netloc,
    'example.com:80',
  )
  assert_equal(
    Url(username='username', password='password', hostname='example.com', port=80).netloc,
    'username:password@example.com:80',
  )

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


class TestSetNetloc():

  def test_set_netloc_on_new_url(self):
    url = Url()
    url.netloc = 'example.com'
    assert_equal(url.username, None)
    assert_equal(url.password, None)
    assert_equal(url.hostname, 'example.com')
    assert_equal(url.port, None)

    url = Url()
    url.netloc = 'user@example.com'
    assert_equal(url.username, 'user')
    assert_equal(url.password, None)
    assert_equal(url.hostname, 'example.com')
    assert_equal(url.port, None)

    url = Url()
    url.netloc = 'user:password@example.com'
    assert_equal(url.username, 'user')
    assert_equal(url.password, 'password')
    assert_equal(url.hostname, 'example.com')
    assert_equal(url.port, None)

    url = Url()
    url.netloc = 'user:password@example.com:80'
    assert_equal(url.username, 'user')
    assert_equal(url.password, 'password')
    assert_equal(url.hostname, 'example.com')
    assert_equal(url.port, 80)

    url = Url()
    url.netloc = '//user:password@example.com:80'
    assert_equal(url.username, 'user')
    assert_equal(url.password, 'password')
    assert_equal(url.hostname, 'example.com')
    assert_equal(url.port, 80)

  def test_overwrite_existing_netloc(self):
    url = Url.from_string('ftp://guest:@ftp.example.com:8000/path/to/my/file.txt')
    url.netloc = 'ftp2.example.com:2100'
    assert_equal(url.username, None)
    assert_equal(url.password, None)
    assert_equal(url.hostname, 'ftp2.example.com')
    assert_equal(url.port, 2100)
    assert_equal(str(url), 'ftp://ftp2.example.com:2100/path/to/my/file.txt')


def test_stringify():
  assert_equal(
    str(Url(scheme='http', username='username', password='password', hostname='example.com', port=80, path='/index.html', fragment='anchor')),
    'http://username:password@example.com:80/index.html#anchor',
  )
  assert_equal(
    str(Url(scheme='http', hostname='example.com', path='/index.html', params='order=random;color=blue', query='sort=foo', fragment='anchor')),
    'http://example.com/index.html;order=random;color=blue?sort=foo#anchor',
  )
  assert_equal(
    str(Url(scheme='http', hostname='example.com', path='/index.html', query='sort=foo', fragment='anchor')),
    'http://example.com/index.html?sort=foo#anchor',
  )


def test_from_string():
  assert_equal(
    Url.from_string('http://example.com/index.html?sort=foo#anchor'),
    Url(scheme='http', hostname='example.com', path='/index.html', query='sort=foo', fragment='anchor'),
  )


def test_repr():
  assert_equal(
    repr(Url(scheme='http', username='username', password='password', hostname='example.com', port=80, path='/index.html', fragment='anchor')),
    "Url(scheme='http', username='username', password='password', hostname='example.com', port=80, path='/index.html', fragment='anchor')",
  )
  assert_equal(
    repr(Url(scheme='http', hostname='example.com', path='/index.html', query='sort=foo&order=desc')),
    "Url(scheme='http', hostname='example.com', path='/index.html', query='sort=foo&order=desc')",
  )
