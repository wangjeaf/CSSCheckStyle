from helper import *

def doTest():
    _basic()
    _one_line_file()
    _with_extra()
    _compress_with_hack_chars()
    _extra_statement()

def _basic():
    msg = doCssFileCompress('_file.css')
    equal(msg, ".test{width:100px;height:200px;_z-index:111}@keyframes 'name'{10% {width:100px}}.another{*width:100px;background-color:#ABC;color:#DDD}", 'file compressed')

def _one_line_file():
    msg = doCssFileCompress('_one_line_file.css')
    equal(msg, ".test{width:100px;height:200px;_z-index:111}@keyframes 'name'{10% {width:100px}}.another{*width:100px;background-color:#ABC;color:#DDD}", 'file compressed')

def _with_extra():
    msg = doCssFileCompress('_with_extra.css')
    equal(msg, "@charset utf-8;@import url('xxxxx');@namespace lalala;.test{width:100px;height:200px;_z-index:111}@import url('xxx2');@import url('xxx3');", 'file compressed')
    
def _compress_with_hack_chars():
    msg = doCssFileCompress('_compress_special_hack_chars.css')
    equal(msg, "li:nth-child(even){background:gray}* html li.even{background:gray}.test[^=aaa]{background:gray}.test1,.test2{width:100px}", 'file compressed')
    
def _extra_statement():
    msg = doCssFileCompress('_extra_statement.css')
    equal(msg, "@-css-compiler{selector-compile:no-combinator;rule-compile:all}@charset utf-8;@-css-compiler-xxx fdasfdas;@import url(fdafdas/fdafdas.css);", 'extra statement compressed')
