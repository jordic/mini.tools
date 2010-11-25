#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.com>
# http://tempointeractiu.es
# License: http://www.opensource.org/licenses/gpl-2.0.php
# version 0.1
# -------------------------------------------------------------------

'''
A little script to convert a set of files encoded in some local format, 
to utf8

Usage:

> to_utf8 directory/ extension enctype_files
    Convert all extension files to utf-8
> to_utf8 directory/ php
    Convert all .php files to utf8

You have to supply third parameter because is very difficult to determine
encodetype with python, for this, you have to determine it, and pass to script
    

- Requires chardet: http://chardet.feedparser.org/
    pip install chardet

- Tested in python 2.6 OSX

'''

import os, glob
import sys
import re
from os.path import abspath, dirname
import codecs
from shutil import move
from chardet.universaldetector import UniversalDetector

if len( sys.argv ) != 3:
    sys.exit('''
Incorrect number of arguments..
=============================================
Usage:

> to_utf8 directory/ extension enctype_files
    Convert all extension files to utf-8
> to_utf8 directory/ php
    Convert all .php files to utf8
You have to supply third parameter because is very difficult to determine
encodetype with python, for this, you have to determine it, and pass to script
    ''')


#print sys.argv
pat = dirname( sys.argv[1] ) 
pattern = sys.argv[2]

#iso-8859-1
enc = "iso-8859-1"
if len(sys.argv) > 3:
    enc = sys.argv[3]
    

def is_utf8( fi ):
    '''
    try to detect if a file is utf_8 using chardet
    '''
    ff = open(fi, 'r')
    detector = UniversalDetector()
    detector.reset()
    for line in ff.readlines():
        detector.feed(line)
        if detector.done: break
    detector.close()
    ff.close()
    if detector.result['encoding'] == 'utf-8':
        return True
    else:
        return None
        

def to_utf8( sourceFileName, enc=enc ):
    targetFileName = "%s.temp" % ( sourceFileName )
    BLOCKSIZE = 1048576 # or some other, desired size in bytes
    with codecs.open(sourceFileName, "r", enc) as sourceFile:
        with codecs.open(targetFileName, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
    os.remove( sourceFileName  )
    move( targetFileName, sourceFileName )



conta = 0
proces = 0
for root, dirs, files in os.walk(pat):
    for name in files:
        if name.endswith(pattern):
            proces = proces +1
            if not is_utf8( os.path.join(root, name) ):
                print "%s converting" % os.path.join(root, name)
                to_utf8( os.path.join(root, name), enc )
                conta = conta + 1
            else:
                print "%s already utf8" % name


print "Total procesats: %s" % proces
print "Total convertides: %s" % conta








