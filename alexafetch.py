import constants
import pycrawl

def fetch():
  pc = pycrawl.PyCrawl(constants.USER_AGENT)
  error = pc.download(constants.ALEXA_URL, "data/alexa/topsites.zip")
  if error is not None:
    print "====\nERROR:\n", error

if __name__=="__main__":
  fetch()
