from helper import *

def doTest():
    go()

def go():
    css = '''.theme-hot li {
    float: left;
    padding: 0 10px 0 2px;
    #padding: 1px 10px 0 2px;
    padding: 1px 10px 0 2px\\0;
    _padding: 3px 10px 0 2px;
}'''

    expectedFixed = '''.theme-hot li {
    float: left;
    padding: 0 10px 0 2px;
    #padding: 1px 10px 0 2px;
    padding: 1px 10px 0 2px\\0;
    _padding: 3px 10px 0 2px;
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), '#padding is ok, do not combine attr which in hack')
    
