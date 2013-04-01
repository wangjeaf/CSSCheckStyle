#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDSingleLineBraces(RuleSetChecker):
    
    '''{
        "summary":"单行的括号检查",
        "desc":"与单行CSS编码风格相关的括号检查"
    }'''

    def __init__(self):
        self.id = 'single-line-brace'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_openingBrace = 'should have "only one space" before the opening brace in "${selector}"'
        self.errorMsg_openingBraceEnd = 'should have "only one space" after the opening brace in "${selector}"'
        self.errorMsg_closingBrace = 'should have "only one space" before the closing brace in "${selector}"'
        self.errorMsg_closingBraceEnd = 'should have "only one space" before the closing brace in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        singleLine = ruleSet.getSingleLineFlag()
        if not singleLine:
            return True
        selector = ruleSet.roughSelector
        if selector.find(',') == -1:
            if selector.endswith('  ') or not selector.endswith(' '):
                self.errorMsg = self.errorMsg_openingBrace
                return False
        else:
            return True

        value = ruleSet.roughValue
        if not value.startswith(' ') or value.startswith('  '):
            self.errorMsg = self.errorMsg_openingBraceEnd
            return False
        if not value.endswith(' ') or value.endswith('  '):
            self.errorMsg = self.errorMsg_closingBraceEnd
            return False
        return True 
