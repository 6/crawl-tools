import constants
import pycrawl
import zipfile

def fetch():
  pc = pycrawl.PyCrawl(constants.USER_AGENT)
  error = pc.download(constants.ALEXA_URL, constants.DATA_PATH_ALEXA)
  if error is not None:
    print "====\nERROR:\n", error
    return
  zip = zipfile.ZipFile(constants.DATA_PATH_ALEXA, "r")
  data = zip.read(constants.ALEXA_CSV_FILE)
  with open(constants.DATA_PATH_ALEXA_CSV, 'wb') as f:
    f.write(data)

if __name__=="__main__":
  fetch()
