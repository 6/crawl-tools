import constants
import pycrawl

class FaviconCrawl(pycrawl.PyCrawl):
  def download(self, base_url):
    url = "http://g.etfv.co/http://{0}?defaulticon=none".format(base_url)
    path = constants.DATA_PATH_FAVICON.format(base_url)
    error = super(FaviconCrawl, self).download(url, path)
    if error is not None:
      print "====\nERROR: {0}\n".format(base_url), error

if __name__=="__main__":
  # basic tests
  fc = FaviconCrawl(constants.USER_AGENT)
  fc.download("www.google.com")
  fc.download("www.nonexistent-website-q3t3qct23tt32.com")
