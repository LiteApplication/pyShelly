# -*- coding: utf-8 -*-
"""Python 2.x and 3.x compability fixes"""

import sys
import urllib.request, urllib.parse, urllib.error

if sys.version_info < (3,):
    import urllib.request, urllib.error, urllib.parse

    def ba2c(x):  # Convert bytearra to compatible string
        return str(x)

    def b(x):
        return bytearray(x)

    def s(x):
        return str(x)

    def uc(x):
        return str(x)

    def urlencode(x):
        return urllib.parse.urlencode(x)

    def urlopen(x):
        return urllib.request.urlopen(x)
else:
    def ba2c(x):  # Convert bytearra to compatible bytearray
        return x

    def b(x):
        return x

    def s(x):
        return str(x, 'cp1252')

    def uc(x):
        return x

    def urlencode(x):
        return urllib.parse.urlencode(x)

    def urlopen(x):
        return urllib.request.urlopen(x)
