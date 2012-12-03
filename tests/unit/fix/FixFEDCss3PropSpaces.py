from helper import *

def doTest():
    fixer, msg = doFix('.test {-webkit-border-radius: 3px;-moz-border-radius:3px;border-radius:3px;}', '')
    equal(msg, '.test {\n    -webkit-border-radius: 3px;\n       -moz-border-radius: 3px;\n            border-radius: 3px;\n}', 'ok')

    fixer, msg = doFix('.test {border-radius:3px;}', '')
    equal(msg, '.test {\n    border-radius: 3px;\n}', 'ok')
