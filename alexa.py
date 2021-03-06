import constants
import random
import publicsuffixparse

class Alexa(object):
  def __init__(self):
    self.domain_parser = publicsuffixparse.parser()
    self.by_rank = {}
    self.by_domain = {}
    with open(constants.DATA_PATH_ALEXA_CSV, 'r') as f:
      for line in f:
        [rank, domain] = self.__parse_line(line)
        if domain is None:
          #print "Invalid: {0}".format(line)
          continue
        self.by_rank[rank] = domain
        self.by_domain[domain] = rank
  
  def __parse_line(self, line):
    vals = line.strip().split(",")
    if len(vals) != 2:
      return [None, None]
    [rank, domain] = vals[0], vals[1]
    if not rank.isdigit():
      return [None, None]
    if "/" in domain:
      # alexa has lots of non-domains near the end of the list
      return [None, None]
    if self.domain_parser.domain(domain) != domain:
      # Ensure domain isn't subdomain or IP address.
      # Actual examples that are now ignored:
      # directoryplaza.cz.cc
      # pretamoda.wordpress.com
      # 195.62.227.104
      # cscartdevelopment.blogspot.in
      return [None, None]
    return [int(rank), domain]
    
  def find_by_rank(self, rank):
    if rank not in self.by_rank:
      return None
    return {"rank": rank, "domain": self.by_rank[rank]}
    
  def find_by_domain(self, domain):
    if domain not in self.by_domain:
      return None
    return {"domain": domain, "rank": self.by_domain[domain]}

  def top(self, how_many):
    sites = []
    rank = 1
    while len(sites) < how_many:
      site = self.find_by_rank(rank)
      if site is not None:
        sites.append(site)
      rank += 1
    return sites

  def random(self, how_many):
    sites = []
    while len(sites) < how_many:
      site = self.find_by_rank(random.randrange(1, 1000001))
      if site is not None:
        sites.append(site)
    return sites

if __name__=="__main__":
  # basic tests
  alexa = Alexa()
  print alexa.find_by_rank(123)
  print alexa.find_by_domain("youtube.com")
  print alexa.top(10)
  print alexa.random(10)
