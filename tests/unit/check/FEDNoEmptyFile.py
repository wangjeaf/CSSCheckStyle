from asserts import ok, equal, notEqual, getResults
from helper import doCssCheck, doCssTextCheck
from ckstyle.reporter.helper import fill

def doTest():
    logs, warns, errors = doCssTextCheck('/* @author: zhifu.wang**/ /* .test {width: 100px;}*/', 'test.css')
    equal(len(errors), 1, 'one error occur')
    equal(fill(errors[0]), 'empty css file "test.css"')

    logs, warns, errors = doCssTextCheck('/* @author: zhifu.wang**/ /* .test {width: 100px;}*/ \n.test { width: 100px; }', 'test.css')
    equal(len(errors), 0, 'no error now')
