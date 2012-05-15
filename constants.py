ALEXA_URL = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
ALEXA_CSV_FILE = "top-1m.csv"
DATA_PATH = "data"
DATA_PATH_ALEXA = "{0}/alexa/topsites.zip".format(DATA_PATH)
DATA_PATH_ALEXA_CSV = "{0}/alexa/{1}".format(DATA_PATH, ALEXA_CSV_FILE)
DATA_PATH_FAVICON = "{0}/favicon/{{0}}.png".format(DATA_PATH)
DATA_PATH_PUBLIC_SUFFIX = "{0}/publicsuffix/publicsuffix.dat".format(DATA_PATH)
DATA_PATH_SCREENSHOT = "{0}/screenshot/".format(DATA_PATH)
PUBLIC_SUFFIX_URL = "http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1"
USER_AGENT = "Mozilla/5.0 (compatible; PyCrawl/0.1)"
