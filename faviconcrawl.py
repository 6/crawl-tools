import pycrawl

class FaviconCrawl(pycrawl.PyCrawl):
  def download(self, base_url):
    url = "http://g.etfv.co/http://{0}?defaulticon=none".format(base_url)
    path = "data/favicon/{0}.png".format(base_url)
    error = super(FaviconCrawl, self).download(url, path)
    if error is not None:
      print "====\nERROR: {0}\n".format(base_url), error

if __name__=="__main__":
  # basic tests
  fc = FaviconCrawl("Mozilla/5.0 (compatible; PyCrawl/0.1)")
  fc.download("www.google.com")
  fc.download("www.nonexistent-website-q3t3qct23tt32.com")
