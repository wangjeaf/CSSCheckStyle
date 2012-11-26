from Base import *
from helper import isCssProp

class FEDUnknownCssNameChecker(RuleChecker):
    def __init__(self):
        self.id = 'unknown-css-prop'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'unknown attribute name "${name}" found in "${selector}"'

    def check(self, rule, config):
        return isCssProp(rule.name.lower())
