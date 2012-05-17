# Wrapper for lib/webkit2png.py for taking screenshots of websites
import constants
import subprocess

def screenshot(url, fname=None, width=1024, height=600, delay=1):
  name_fmt = "" if fname is None else " --filename={0}".format(fname)
  cmd = "python vendor/webkit2png/webkit2png {0} -W {1} -H {2} --fullsize --delay={3}{4} --dir={5}".format(url, width, height, delay, name_fmt, constants.DATA_PATH_SCREENSHOT)
  subprocess.call(cmd, shell=True)

if __name__=="__main__":
  screenshot("http://www.google.jp", "google.jp")
