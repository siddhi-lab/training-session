import math
import sys

size_bytes = sys.argv[1]

size_bytes = int(size_bytes)
def convert_size(size_bytes):
  if size_bytes == 0:
    return "0B"
  else:    
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(int(size_bytes) / int(p), 2)
    print("cap in GB:", s)
    print("size name:", size_name[i])
    return "%s %s" % (s, size_name[i])

if __name__ == "__main__":
  #main()
  convert_size(size_bytes)
