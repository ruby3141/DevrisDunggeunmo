import os, sys
from fontTools.ttLib import TTFont

name, ext = os.path.splitext(sys.argv[1])
f = TTFont(sys.argv[1])

f.flavor='woff'
f.save(name + '.woff')

f.flavor='woff2'
f.save(name + '.woff2')