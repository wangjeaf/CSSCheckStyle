from helper import *

def doTest():
    _basic()
    _with_hack()
    _with_extra()
    _with_different_level()
    _with_css3_props()

def _basic():
    msg = doCssCompress('/* @wangjeaf */ .test {width: 100px; display:none; height: 100px;}')
    equal(msg, '.test{display:none;width:100px;height:100px}', 'general order compress is ok')

def _with_hack():
    msg = doCssCompress('.test {_width: 100px; *display:none;_display:none;display:block\9;*height: 100px;}')
    equal(msg, '.test{*display:none;_display:none;display:block\9;_width:100px;*height:100px}', 'hack order compress is ok')

def _with_extra():
    msg = doCssCompress('@import (url-here);.test {_width: 100px; *height: 100px;}')
    equal(msg, '@import (url-here);.test{_width:100px;*height:100px}', 'extra order compress is ok')

def _with_different_level():
    msg = doCssCompress('.test {cursor:pointer;color:red;line-height:10px;background-color:red;margin-top:10px;padding-bottom:10px;position:relative;}')
    equal(msg, '.test{position:relative;margin-top:10px;padding-bottom:10px;background-color:red;line-height:10px;color:red;cursor:pointer}', 'different levels is ok')

def _with_css3_props():
    msg = doCssCompress('.test {-moz-transform:xxxx;-webkit-transform:xxxx;transform:xxxx;*zoom:1;width:100px;display:none;}')
    equal(msg, '.test{display:none;width:100px;*zoom:1;-moz-transform:xxxx;-webkit-transform:xxxx;transform:xxxx}', 'different levels is ok')
