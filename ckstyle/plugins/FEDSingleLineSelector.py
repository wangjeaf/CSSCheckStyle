from Base import *

class FEDSingleLineSelector(RuleSetChecker):
    def __init__(self):
        self.id = 'single-line-selector'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_noEnterInSingleSelector = 'should not "enter" at the end of "${selector}"'
        self.errorMsg_multiSelectorBeforeSemicolon = 'should not have "space" after semicolon in "${selector}"'
        self.errorMsg_shouldNotStartsWithSpace = 'should start with "space" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.roughSelector
        if selector.find(',') != -1:
            return True

        if selector.lstrip().find('\n') != -1:
            self.errorMsg = self.errorMsg_noEnterInSingleSelector
            return False

        splited = selector.split('\n')
        realSelector = splited[len(splited) - 1]
        
        if realSelector.startswith(' '):
            self.errorMsg = self.errorMsg_shouldNotStartsWithSpace
            return False

        return True 
