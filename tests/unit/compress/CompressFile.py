from helper import *

def doTest():
    _basic()
    _one_line_file()

def _basic():
    msg = doCssFileCompress('_file.css')
    equal(msg, ".test{width:100px;height:200px;_z-index:111}@keyframes 'name'{10% {width: 100px;}}.another{*width:100px;color:#DDD;background-color:#ABC}", 'file compressed')

def _one_line_file():
    msg = doCssFileCompress('_one_line_file.css')
    equal(msg, ".test{width:100px;height:200px;_z-index:111}@keyframes 'name'{10% {width: 100px;}}.another{*width:100px;color:#DDD;background-color:#ABC}", 'file compressed')
