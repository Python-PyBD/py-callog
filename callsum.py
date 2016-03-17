#!/usr/bin/env python

import sys

sec = 0

for line in sys.stdin:
    h, m, s = line.strip().split(':')
    sec += int(h) * 3600 + int(m) * 60 + int(s)
    
h, m = divmod(sec, 3600)
m, s = divmod(m, 60)

print "%dh %dm %ds" % (h, m, s)
