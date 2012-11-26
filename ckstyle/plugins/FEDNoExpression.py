from Base import *

class FEDNoExpression(RuleChecker):
    def __init__(self):
        self.id = 'no-expression'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_use = 'should not use expression in "${selector}" '
        self.errorMsg_hack = 'should add hack for expression in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        value = rule.value
        name = rule.name
        replaced = value.replace(' ', '')

        if value.find('expression') == -1:
            return True

        if replaced.find('Expressions') != -1:
            if rule.name == rule.roughName.strip():
                self.errorMsg = self.errorMsg_hack
                return False
            return True

        if replaced.find('this.style.' + name + '=') != -1:
            if rule.name == rule.roughName.strip():
                self.errorMsg = self.errorMsg_hack
                return False
            return True

        self.errorMsg = self.errorMsg_use
        return False
