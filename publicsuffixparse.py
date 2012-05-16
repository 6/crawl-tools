import constants
import gitmodules
gitmodules.add_vendor()
import publicsuffix

def parser():
  #TODO incorrectly ignore "private domains", e.g. dyndns, centralnic, etc
  with open(constants.DATA_PATH_PUBLIC_SUFFIX, 'r') as f:
    return publicsuffix.SuffixList(f.read().splitlines())

if __name__=="__main__":
  dv = parser()
  if dv is not None:
    url = "abc.d-e-f.example.co.uk"
    print dv.domain(url)
    print dv.tld(url)
    print dv.parents(url)
