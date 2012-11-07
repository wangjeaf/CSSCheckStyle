from Base import *
from helper import isFontFamilyName

class FEDCanNotSetFontFamily(RuleChecker):
    def __init__(self):
        self.id = 'no-font-family'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'can not set font-family for "${selector}"'

    def check(self, rule):
        if rule.name == 'font-family':
            return False

        if rule.name == 'font':
            # many fonts
            if rule.value.find(',') != -1:
                return False

            # one font
            splited = rule.value.split(' ')
            if isFontFamilyName(splited[len(splited) - 1]):
                return False

        return True
