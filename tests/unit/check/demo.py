from helper import *
from ckstyle.reporter.helper import fill

def doTest():
    text = 'body {width: 1px}'
    logs, warns, errors = doCssCheck(text)
    equal(len(logs), 2, 'two logs')
    equal(len(warns), 1, 'one warn happened')
    equal(len(errors), 1, 'one error happened')
    equal(fill(warns[0]), r'each rule in "body" need semicolon in the end, "width" has not', 'warn rule text is ok')
    equal(fill(errors[0]), r'should not set style for html tag in "body"', 'error rule text is ok')
