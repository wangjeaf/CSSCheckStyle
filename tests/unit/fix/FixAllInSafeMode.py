from helper import *
from helper import *

def doTest():
    _singleLine()
    _multiLine()

def _singleLine():
    defaultConfig.safeMode = True
    fixer, msg = doFix('.test {width:"100px";color:#DDDDDD;margin:0 auto 0 auto;} .test2 {width:"100px";color:#DDDDDD;margin-top:0;margin-left:auto;margin-right:auto;margin-bottom:0;}', fileName = '', config = defaultConfig)
    defaultConfig.safeMode = False
    equal(msg, 
'''.test {
    width: '100px';
    margin: 0 auto;
    color: #DDD;
}

.test2 {
    width: '100px';
    margin: 0 auto;
    color: #DDD;
}''', 'safe mode true, fix is ok')

def _multiLine():
    fixer, msg = doFix('.test {width:"100px";color:#DDDDDD;margin:0 auto 0 auto;} .test2 {width:"100px";color:#DDDDDD;margin-top:0;margin-left:auto;margin-right:auto;margin-bottom:0;}', '')
    equal(msg, 
'''.test,
.test2 {
    width: '100px';
    margin: 0 auto;
    color: #DDD;
}''', 'default safeMode is false, fix is ok')
