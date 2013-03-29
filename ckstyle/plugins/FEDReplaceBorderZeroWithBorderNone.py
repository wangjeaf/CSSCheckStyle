#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDReplaceBorderZeroWithBorderNone(RuleChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
    }'''

    def __init__(self):
        self.id = 'no-border-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_borderWidth = 'replace "border-width: 0" with "border-width: none" in "${selector}"'
        self.errorMsg_border = 'replace "border: 0" with "border: none" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        if rule.name == 'border' and rule.value == '0':
            self.errorMsg = self.errorMsg_border
            return False

        if rule.name == 'border-width' and rule.value == '0':
            self.errorMsg = self.errorMsg_borderWidth
            return False

        return True
