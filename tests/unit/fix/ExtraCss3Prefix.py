from helper import *

def doTest():
    css = '''.html {
        -moz-box-sizing: 1px;
        -webkit-box-sizing: 1px;
        box-sizing: 1px;
    }'''

    expectedFixed = '''.html {
    -webkit-box-sizing: 1px;
       -moz-box-sizing: 1px;
            box-sizing: 1px;
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'css3 prefix box-sizing is ok')
