#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoExpression(RuleChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
    }'''

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

        if replaced.find('Expressions') != -1 or replaced.find('this.style.' + name + '=') != -1 or replaced.find('this.runtimeStyle.' + name + '=') != -1:
            if rule.name == rule.strippedName:
                selector = rule.selector.replace(' ', '')
                if selector.find('*html') == -1:
                    self.errorMsg = self.errorMsg_hack
                    return False
            return True

        self.errorMsg = self.errorMsg_use
        return False
