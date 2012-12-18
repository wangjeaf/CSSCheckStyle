from helper import *

def doTest():
    css = '''/*fdafda*/
.page-title {
   width: 100px;
   padding: 0px 1px;
}

.page-title {
   width: 100px;
   padding: 0px 1px;
}'''

    expected = '''/* fdafda */
.page-title {
    width: 100px;
    padding: 0 1px;
}'''
    fixer, msg = doFix(css, '')
    equal(msg, expected, 'it is the same ruleset');
