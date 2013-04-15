#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDFontSizeShouldBePtOrPx(RuleChecker):
    
    '''{
        "summary":"字体的单位必须用px或pt",
        "desc":"字体的单位可以有很多种，比如 <code>px pt em %</code> 等等，为了统一取值，统一要求为 <code>px/pt</code> ， 例如：<br>
            <code>font-size: 12px;</code><br>
            <code>font-size: 14pt;</code>"
    }'''

    def __init__(self):
        self.id = 'font-unit'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_ptOrPx = 'font-size unit should be px/pt in "${selector}"'
        self.errorMsg_xsmall = 'font-size should not be small/medium/large in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        if rule.name != 'font-size':
            return True

        value = rule.value
        if value.find('small') != -1 or value.find('medium') != -1 or value.find('large') != -1:
            self.errorMsg = self.errorMsg_xsmall
            return False

        if value == '0':
            return True

        if value.endswith('pt'):
            return True

        if value.endswith('px'):
            return True

        self.errorMsg = self.errorMsg_ptOrPx
        return False
