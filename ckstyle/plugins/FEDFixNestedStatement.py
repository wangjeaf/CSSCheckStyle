#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDFixNestedStatement(ExtraChecker):
    
    '''{
        "summary":"修复嵌套的CSS",
        "desc":"@keyframes, @media之类的"
    }'''

    def __init__(self):
        self.id = 'fix-nested-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''
        self.always = True

    def check(self, ruleSet, config):
        return True

    def fix(self, ruleSet, config):
        if not ruleSet.nested:
            return
        ruleSet.fixedSelector = ruleSet.fixedSelector.replace('"', '\'')
        statement = ruleSet.fixedStatement
        from ckstyle.doCssFix import doFix
        checker, msg = doFix(statement, '', config)
        ruleSet.fixedStatement = msg
