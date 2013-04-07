from helper import *

def doTest():
    _basic()

def _basic():
    checker = doCssFileCompress2('_browsers.css')
    equal('a{width:300px}', checker.doCompress(STD), 'std is ok')
    equal('*html a{width:100px}a{width:300px;_width:400px}', checker.doCompress(STD | IE6), 'ie6 is ok')
    equal('*+html a{width:200px}a{width:300px}', checker.doCompress(STD | IE7), 'ie7 is ok')