from Base import *
import re
pattern = re.compile('\d+')

class FEDNoSimpleNumberInSelector(RuleSetChecker):
    def __init__(self):
        self.id = 'number-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'do not simply use 1,2,3 as selector(use v1/step1/item1), in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector

        if selector.find('@media') != -1:
            return True
            
        found = pattern.findall(selector)
        for x in found:
            if selector.find('v' + x) == -1 and selector.find('step' + x) == -1  and selector.find('item' + x) == -1 and selector.find('h' + x) == -1 :
                return False
        return True 
