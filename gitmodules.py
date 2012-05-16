import os
import sys

# based on: http://stackoverflow.com/a/5137737/223408
def add_vendor():
  vendor = 'vendor'
  for dir in os.listdir(vendor):
    path = os.path.join(vendor, dir)
    if not path in sys.path:
      sys.path.append(path)
