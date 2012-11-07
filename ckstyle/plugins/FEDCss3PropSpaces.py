from Base import *
from helper import isCss3Prop, isCss3PrefixProp

class FEDCss3PropSpaces(RuleChecker):
    def __init__(self):
        self.id = 'css3-prop-spaces'

        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'css3 prop "${name}" should align to right in "${selector}"'

    def check(self, rule):
        name = rule.name
        # only for css3 props
        if not isCss3Prop(name):
            return True

        if not isCss3PrefixProp(name):
            return True
        
        roughName = rule.roughName
        # 12 = 4 + 8, 4 spaces, 8 for align
        if len(roughName.split(name)[0]) != 12:
            return False
        return True
