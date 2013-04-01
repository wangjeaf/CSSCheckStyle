#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDUseLowerCaseSelector(RuleSetChecker):
    
    '''{
        "summary":"选择器用小写字母",
        "desc":"选择器应该用小写字母， 例如 <code>.demo</code> ， 不允许使用大写，例如： <code>.Demo .Test</code>"
    }'''

    def __init__(self):
        self.id = 'lowercase-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'selector should use lower case, in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.lower() != selector:
            return False

        return True 

    def fix(self, ruleSet, config):
        # if fix upper to lower, will cause error in HTML(do not do evil)
        pass
        #selector = ruleSet.selector
        #if selector.lower() != selector:
        #    ruleSet.fixedSelector = ruleSet.fixedSelector.lower()
