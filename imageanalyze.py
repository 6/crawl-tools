import numpy
from PIL import Image
import constants
import gitmodules
gitmodules.add_vendor()
import colorific

def numpy_array_of(image_path):
  return numpy.array(Image.open(image_path))

def dimensions(image_path):
  shape = numpy_array_of(image_path).shape
  # returns (width, height)
  return (shape[1], shape[0])

# n_quantized: start with an adaptive palette of this size
# min_distance: min distance to consider two colors different
# min_prominence: ignore if less than this proportion of image
# min_saturation: ignore if not saturated enough
# max_colors: keep only this many colors
def palette(image_path, min_saturation=0.05, min_prominence=0.01,
              min_distance=10.0, max_colors=5, n_quantized=100):
  colorp = colorific.extract_colors(image_path, min_saturation=min_saturation,
    min_prominence=min_prominence, min_distance=min_distance,
    max_colors=max_colors, n_quantized=n_quantized)
  return [colorific.rgb_to_hex(c.value) for c in colorp.colors]

if __name__=="__main__":
  print dimensions(constants.DATA_PATH_SCREENSHOT_FILE.format("google.jp"))
  print palette(constants.DATA_PATH_FAVICON.format("www.google.com"))
