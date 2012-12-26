from Base import *

class FEDFixNestedStatement(ExtraChecker):
    def __init__(self):
        self.id = 'fix-nested-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''

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
