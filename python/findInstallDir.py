import sys
import sysconfig

path = sysconfig.get_path("purelib")

sys.stdout.write(path)