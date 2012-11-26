from Base import *
from helper import containsChnChar

class FEDTransChnFontFamilyNameIntoEng(RuleChecker):
    def __init__(self):
        self.id = 'no-chn-font-family'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'should not use chinese font family name in "${selector}"'

    def check(self, rule, config):
        if rule.name != 'font' and rule.name != 'font-family':
            return True

        if containsChnChar(rule.value):
            return False

        return True 
