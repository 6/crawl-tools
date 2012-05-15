import cookielib
import urllib2

class PyCrawl(object):
  def __init__(self, user_agent=None):
    cj = cookielib.CookieJar()
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    if user_agent is not None:
      self.opener.addheaders = [('User-agent', user_agent)]

  def get(self, url):
    error, result = None, None
    try:
      result = self.opener.open(url)
      info = result.info().dict
      if 'content-length' in info and info['content-length'] is '0':
        raise CrawlError("204: No content")
    except ValueError:
      error = "Invalid URL value"
    except urllib2.URLError as e:
      error = e
    except CrawlError as e:
      error = e
    return [error, result]

  def download(self, url, path):
    [error, result] = self.get(url)
    if error is not None:
      return error
    with open(path, 'wb') as f:
      f.write(result.read())

class CrawlError(Exception):
  def __init__(self, value):
    self.parameter = value
  def __str__(self):
    return repr(self.parameter)
