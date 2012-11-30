from helper import *

def doTest():
    equal(getFixed('.test {margin:0 0 0 0}', 'margin'), '0', 'margin is fixed')
    equal(getFixed('.test {margin:0 auto 0 auto}', 'margin'), '0 auto', 'margin two is fixed')
    equal(getFixed('.test {margin:auto 0 0 auto}', 'margin'), 'auto 0 0 auto', 'margin three is fixed')
    equal(getFixed('.test {margin:0 0}', 'margin'), '0', 'margin four is fixed')
    equal(getFixed('.test {margin:0px 0}', 'margin'), '0', 'margin four is fixed')
    equal(getFixed('.test {margin:0px 1px 0px 1px}', 'margin'), '0 1px', 'margin four is fixed')
    equal(getFixed('.test {margin:0px auto 0px auto}', 'margin'), '0 auto', 'margin four is fixed')
