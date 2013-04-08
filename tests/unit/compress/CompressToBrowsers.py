from helper import *

def doTest():
    _basic()
    _combine()

def _basic():
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-webkit-transform:1s;-moz-transform:1s;-o-transform:1s}b{width:300px;-moz-transform:1s}', checker.doCompress(STD | NONEIE), 'std is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-webkit-transform:1s}b{width:300px}', checker.doCompress(STD | WEBKIT), 'webkit is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-o-transform:1s}b{width:300px}', checker.doCompress(STD | OPERA), 'opera is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-webkit-transform:1s}b{width:300px}', checker.doCompress(STD | CHROME), 'chrome is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-moz-transform:1s}b{width:300px;-moz-transform:1s}', checker.doCompress(STD | FIREFOX), 'firefox is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('*html a{width:100px}b{width:300px;_width:400px}', checker.doCompress(STD | IE6), 'ie6 is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('*+html a{width:200px}b{width:300px}', checker.doCompress(STD | IE7), 'ie7 is ok')

def _combine():
	checker = doCssFileCompress2('_browsers_combine_ruleset.css')
	equal('a,b,d{width:300px;-moz-transform:1s}', checker.doCompress(STD | FIREFOX), 'firefox is ok')
	checker = doCssFileCompress2('_browsers_combine_ruleset.css')
	equal('a{width:300px;-webkit-transform:1s}b,d{width:300px}', checker.doCompress(STD | CHROME), 'chrome 2 is ok')