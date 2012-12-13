from helper import *

def doTest():
    _singleLine()
    _multiLine()

def _singleLine():
    defaultConfig.fixToSingleLine = True
    fixer, msg = doFix('.test {width:"100px";color:#DDDDDD;} .test2 {width:"100px";color:#DDDDDD;}', fileName = '', config = defaultConfig)
    defaultConfig.fixToSingleLine = False
    equal(msg, '''.test,
.test2 { width: '100px'; color: #DDD; }''', 'fix to single line is ok')

def _multiLine():
    fixer, msg = doFix('.test {width:"100px";color:#DDDDDD;} .test2 {width:"100px";color:#DDDDDD;}', '')
    equal(msg, '''.test,
.test2 {
    width: '100px';
    color: #DDD;
}''', 'fix to multi line is ok')
