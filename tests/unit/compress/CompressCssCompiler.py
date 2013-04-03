from helper import *

def doTest():
    _no_space()
    _has_space()
    _just_prefix()

def _no_space():
    msg = doCssCompress('@-css-compiler{selector-compile:no-combinator;rule-compile:all}html{width:100px;}')
    equal(msg, 'html{width:100px}', '@css-compiler compressed')

def _has_space():
    msg = doCssCompress('@-css-compiler   {selector-compile:no-combinator;rule-compile:all}html{width:100px;}')
    equal(msg, 'html{width:100px}', '@css-compiler compressed')

def _just_prefix():
    msg = doCssCompress('@-css-compiler-prefix fdsafdsafdsa;html{width:100px;}')
    equal(msg, 'html{width:100px}', '@css-compiler compressed')