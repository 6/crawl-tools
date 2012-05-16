import constants
import pycrawl
import zipfile

def fetch():
  pc = pycrawl.PyCrawl(constants.USER_AGENT)
  error = pc.download(constants.ALEXA_URL, constants.DATA_PATH_ALEXA)
  if error is not None:
    print "====\nERROR:\n", error
    return
  zipf = zipfile.ZipFile(constants.DATA_PATH_ALEXA, "r")
  data = zipf.read(constants.ALEXA_CSV_FILE)
  with open(constants.DATA_PATH_ALEXA_CSV, 'wb') as f:
    f.write(data)

if __name__=="__main__":
  fetch()
