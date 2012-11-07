from Base import *
from helper import isCss3PrefixProp

class FEDMultiLineSpaces(RuleChecker):
    def __init__(self):
        self.id = 'multi-line-space'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_name_pre = 'should have 4 spaces before "${name}" in "${selector}"'
        self.errorMsg_name_after = 'should not have "space" after "${name}" in "${selector}"'
        self.errorMsg_value_pre = 'should have (only) one "space" before value of "${name}" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule):
        singleLine = rule.getRuleSet().getSingleLineFlag()
        if singleLine:
            return True
        
        prefix = ' ' * 4
        name = rule.roughName
        value = rule.roughValue
        stripped = rule.roughName.strip()

        # leave special css3 props for FEDCss3AttrChecker
        if isCss3PrefixProp(rule.name):
            if name.endswith(' '):
                self.errorMsg = self.errorMsg_name_after
                return False

            if not value.startswith(' ') or value.startswith('  '):
                self.errorMsg = self.errorMsg_value_pre
                return False

            return True

        if name.find('\t') != -1:
            name = name.replace('\t', prefix)
        if not name.startswith(prefix):
            self.errorMsg = self.errorMsg_name_pre
            return False
        if name.startswith(' ' * 5):
            self.errorMsg = self.errorMsg_name_pre
            return False
        if name.endswith(' '):
            self.errorMsg = self.errorMsg_name_after
            return False

        if not value.startswith(' ') or value.startswith('  '):
            self.errorMsg = self.errorMsg_value_pre
            return False

        return True 
