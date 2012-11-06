from Base import *
import string
from helper import isCss3PrefixProp

class FEDZIndexShouldInRange(RuleChecker):
    def __init__(self):
        self.id = 'z-index-in-range'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'value of "z-index" is not correct in "${selector}"'

    def check(self, rule):
        if rule.name != 'z-index':
            return True

        zIndex = None
        try:
            zIndex = string.atoi(rule.value)
        except ValueError:
            return False

        if zIndex < -1:
            return False

        if zIndex > 2100:
            return False

        return True 
