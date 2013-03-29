#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDShouldNotUseImportant(RuleChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
    }'''

    def __init__(self):
        self.id = 'do-not-use-important'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'Should not use !important in "${name}" of "${selector}"'

    def check(self, rule, config):
        value = rule.value
        if value.replace(' ', '').find('!important') != -1:
            return False
        return True 
