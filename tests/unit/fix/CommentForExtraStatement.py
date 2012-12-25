from helper import *

def doTest():
    _with_comment()
    _without_comment()

def _with_comment():
    css = '''/**
 * @descript: topic pages
 * @author: ming.zhou
 * @date: 2012-12-7
 */

@import url(dfafdas);

@import url(dfafdas);'''

    expectedFixed = '''/**
 * @descript: topic pages
 * @author: ming.zhou
 * @date: 2012-12-7
 */
@import url(dfafdas);

@import url(dfafdas);
'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'extra statement with comment is ok')
    
def _without_comment():
    css = '''

@import url(dfafdas);

@import url(dfafdas);'''

    expectedFixed = '''@import url(dfafdas);

@import url(dfafdas);
'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'extra statement without comment is ok')
    
