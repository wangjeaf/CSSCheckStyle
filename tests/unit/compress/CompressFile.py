from helper import *

def doTest():
    _basic()
    _one_line_file()
    _with_extra()

def _basic():
    msg = doCssFileCompress('_file.css')
    equal(msg, ".test{width:100px;height:200px;_z-index:111}@keyframes 'name'{10% {width: 100px;}}.another{*width:100px;color:#DDD;background-color:#ABC}", 'file compressed')

def _one_line_file():
    msg = doCssFileCompress('_one_line_file.css')
    equal(msg, ".test{width:100px;height:200px;_z-index:111}@keyframes 'name'{10% {width: 100px;}}.another{*width:100px;color:#DDD;background-color:#ABC}", 'file compressed')

def _with_extra():
    msg = doCssFileCompress('_with_extra.css')
    equal(msg, "@charset utf-8;@import url('xxxxx');@namespace lalala;.test{width:100px;height:200px;_z-index:111}@import url('xxx2');@import url('xxx3');", 'file compressed')
    
