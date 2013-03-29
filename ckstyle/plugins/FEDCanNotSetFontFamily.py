#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isFontFamilyName

class FEDCanNotSetFontFamily(RuleChecker):
    
    '''{
        "summary":"不允许业务代码设置字体",
        "desc":"由于业务代码中随意设置字体，导致字体取值混乱，因此不允许随意在业务代码中设置字体"
    }'''

    def __init__(self):
        self.id = 'no-font-family'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'can not set font-family for "${selector}"'

    def check(self, rule, config):
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
