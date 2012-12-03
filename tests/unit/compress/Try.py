from helper import *

def doTest():
    _basic()
    _with_hack()
    _with_extra()
    _with_keyframes()
    _with_keyframes_enter()
    _only_comments()

def _basic():
    msg = doCssCompress('/* @wangjeaf */ .test {width: 100px; height: 100px;}')
    equal(msg, '.test{width:100px;height:100px}', 'compressed')

def _with_hack():
    msg = doCssCompress('.test {_width: 100px; *height: 100px;}')
    equal(msg, '.test{_width:100px;*height:100px}', 'hack compressed')

def _with_extra():
    msg = doCssCompress('@import (url-here);.test {_width: 100px; *height: 100px;}')
    equal(msg, '@import (url-here);.test{_width:100px;*height:100px}', 'extra compressed')

def _with_keyframes():
    msg = doCssCompress('@keyframes "test"{ \n10% {\nwidth:100px;\n} 60% {\nwidth: 200px;\n}}')
    equal(msg, '@keyframes "test"{10% {width:100px} 60% {width:200px}}', 'keyframes compressed')

def _with_keyframes_enter():
    msg = doCssCompress('''
@keyframes .fdasfads {
    10% {
        width: 200px;
    }

    20% {
        width: 200px;
    }
}''')
    equal(msg, '@keyframes .fdasfads{10% {width:200px}20% {width:200px}}', 'keyframes compressed')

def _only_comments():
    msg = doCssCompress('/* a */ /* a */ /* a */ /* a */')
    equal(msg, '', 'nothing')
