from Base import *

class FilterForIEShouldHack(RuleChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'filter only working for IE should add css hack'
    def check(self, rule):
        if rule.name == 'filter' and rule.value.find('Microsoft') != -1:
            if rule.roughName.strip() == rule.name:
                return False
        return True 
