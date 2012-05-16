import constants
import gitmodules
gitmodules.add_vendor()
import publicsuffix

def parser():
  publicsuffix.init_suffix_tree(constants.DATA_PATH_PUBLIC_SUFFIX)
  return publicsuffix.suffixtree

if __name__=="__main__":
  dv = parser()
  if dv is not None:
    url = "abc.d-e-f.example.co.uk"
    print dv.domain(url)
