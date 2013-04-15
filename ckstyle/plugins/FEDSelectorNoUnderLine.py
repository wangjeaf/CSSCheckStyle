#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDSelectorNoUnderLine(RuleSetChecker):
    
    '''{
        "summary":"不要在选择器中使用下划线",
        "desc":"在selector中不要使用下划线 <code>_</code> ，可以使用中划线 <code>-</code>"
    }'''

    def __init__(self):
        self.id = 'no-underline-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'should not use _ in selector "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.find('_') != -1:
            return False
        return True 
