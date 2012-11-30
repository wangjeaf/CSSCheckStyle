from helper import *

def doTest():
    equal(getFixed('.test {margin:0 0 0 0}', 'margin'), '0', 'margin is fixed')
    equal(getFixed('.test {margin:0 auto 0 auto}', 'margin'), '0 auto', 'margin 2 is fixed')
    equal(getFixed('.test {margin:auto 0 0 auto}', 'margin'), 'auto 0 0 auto', 'margin 3 is fixed')
    equal(getFixed('.test {margin:0 0}', 'margin'), '0', 'margin 4 is fixed')
    equal(getFixed('.test {margin:0px 0}', 'margin'), '0', 'margin 5 is fixed')
    equal(getFixed('.test {margin:0px 1px 0px 1px}', 'margin'), '0 1px', 'margin 6 is fixed')
    equal(getFixed('.test {margin:0px auto 0px auto}', 'margin'), '0 auto', 'margin 7 is fixed')
    equal(getFixed('.test {margin:50px auto 0 auto}', 'margin'), '50px auto 0', 'margin 8 is fixed')
    equal(getFixed('.test {margin: -15px -15px 0 -15px}', 'margin'), '-15px -15px 0', 'margin 9 is fixed')
