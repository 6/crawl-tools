import os
import sys

# based on: http://stackoverflow.com/a/5137737/223408
def add_vendor():
  vendor = 'vendor'
  for directory in os.listdir(vendor):
    path = os.path.join(vendor, directory)
    if not path in sys.path:
      sys.path.append(path)
