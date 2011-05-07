#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.com>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
A little tool to change creation time and modification time 
from a given directory... 
Usued to normalize timezones in camera photos during travels...
'''

import os, glob
import sys
import re
from os.path import abspath, dirname
from stat import ST_ATIME, ST_MTIME


if len(sys.argv)<2:
    print """----------------------------
Usage: change_time directory timedelta
timedelta in milliseconds
For example:
    change_time.py ./ -25200 
    will change time minus 7 hours
    """
    sys.exit(0)

pat = dirname( sys.argv[1] )
delta_time = int( sys.argv[2] )

#print "Modificamos el tiempo en: %s" % delta_time
conta = 0
for root, dirs, files in os.walk(pat):
    for name in files:
        try:
            stat = os.stat(os.path.join(root, name))
            t = stat[ST_ATIME] + delta_time
        except os.error:
            sys.stderr.write(name + ': cannot stat\n')
            sys.exit(2)
        try:
            os.utime(os.path.join(root, name), (t,t))
        except os.error:
            sys.stderr.write(file2 + ': cannot change time\n')
            sys.exit(2)
        conta
print "============================================\n%s files treated\n" % conta

