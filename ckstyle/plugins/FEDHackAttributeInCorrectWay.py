from Base import *
from helper import isCss3PrefixProp

class FEDHackAttributeInCorrectWay(RuleChecker):
    def __init__(self):
        self.id = 'hack-prop'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = '"${name}" is not in correct hacking way in "${selector}"'

    def check(self, rule):
        if rule.value.find(r'\0') != -1:
            return False

        stripped = rule.roughName.strip()
        if rule.name == stripped.lower():
            return True

        if isCss3PrefixProp(rule.name):
            return True

        if not stripped.startswith('_') and not stripped.startswith('*') and not stripped.startswith('+'):
            return False

        return True 
