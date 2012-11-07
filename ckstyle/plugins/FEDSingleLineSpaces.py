from Base import *

class FEDSingleLineSpaces(RuleChecker):
    def __init__(self):
        self.id = 'single-line-space'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_noSpace = 'should have one "space" before "${name}" in "${selector}"'
        self.errorMsg_spaceEnd = 'should not have "space" after "${name}" in "${selector}"'
        self.errorMsg_noSpaceBeforeValue = 'should have one "space" before value of "${name}" in "${selector}"'
        self.errorMsg_extraSpaceAfterValue = 'found extra "space" after value of "${name}" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule):
        singleLine = rule.getRuleSet().getSingleLineFlag()
        if not singleLine:
            return True

        if not rule.roughName.startswith(' '):
            self.errorMsg = self.errorMsg_noSpace
            return False

        if rule.roughName.endswith(' '):
            self.errorMsg = self.errorMsg_spaceEnd
            return False
        
        if not rule.roughValue.startswith(' '):
            self.errorMsg = self.errorMsg_noSpaceBeforeValue
            return False

        value = rule.roughValue.strip()
        if value.endswith(' ;') or value.endswith(' '):
            self.errorMsg = self.errorMsg_extraSpaceAfterValue
            return False

        return True 
