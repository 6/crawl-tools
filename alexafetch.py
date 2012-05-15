import constants
import pycrawl

def fetch():
  pc = pycrawl.PyCrawl(constants.USER_AGENT)
  error = pc.download(constants.ALEXA_URL, constants.DATA_PATH_ALEXA)
  if error is not None:
    print "====\nERROR:\n", error

if __name__=="__main__":
  fetch()
