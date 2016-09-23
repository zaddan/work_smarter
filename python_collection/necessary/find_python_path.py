import os
from pprint import pprint
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print user_paths

# import sys
# map(pprint,sys.path)
