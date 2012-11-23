from helper import *

def doTest():
    msg = doCssFileCompress('_test.css')
    equal(msg, '@import (url-here);.test,.test2,.test3,.test4,.test5{_width:100px;*height:100px}.test6{display:none;_width:100px;*height:100px}', 'totally compressed')

    msg = doCssFileCompress('_test_different_order.css')
    equal(msg, '.test1,.test2,.test3,.test4,.test5{*display:none;_display:inline-block;width:100px;height:200px;border:1px solid #FFF}', 'totally compressed')
