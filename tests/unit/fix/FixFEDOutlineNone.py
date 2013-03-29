from helper import *

def doTest():
    _try()

def _try():
    fixer, msg = doFix('.test {outline:none;}', '')
    equal(msg, '''.test {
    outline: 0;
}''', 'outline fix ok')
