from helper import *

def doTest():
    _not_listed()
    _both_not_listed()

def _both_not_listed():
    css = '''html {
  -webkit-hyphens: auto;
  -moz-hyphens: auto;
  -ms-hyphens: auto;
  -o-hyphens: auto;
  hyphens: auto;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}'''

    expectedFixed = '''html {
    -webkit-hyphens: auto;
       -moz-hyphens: auto;
        -ms-hyphens: auto;
         -o-hyphens: auto;
            hyphens: auto;
    -webkit-user-select: none;
       -moz-user-select: none;
        -ms-user-select: none;
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'both css3 prop not listed is ok')
    
def _not_listed():
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
