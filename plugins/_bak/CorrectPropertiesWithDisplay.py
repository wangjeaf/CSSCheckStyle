from Base import *

class CorrectPropertiesWithDisplay(RuleChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_float = 'display:inline-block should not use float in "${selector}"'
        self.errorMsg_verticalAlign = 'display:block should not use vertical-align in "${selector}"'
        self.errorMsg_tableXXX = 'display:table-* should not use margin or float in "${selector}"'
        self.errorMsg_inline = 'display:inline should not use width,height,margin,margin-top,margin-bottom,float in "${selector}"'
        self.errorMsg = ''

    def check(self, rule):
        name = rule.name
        if name != 'display':
            return True

        ruleSet = rule.getRuleSet()
        if rule.value == 'inline-block' and ruleSet.getRuleByName('float') is not None:
            self.errorMsg = self.errorMsg_float
            return False

        if rule.value == 'block' and ruleSet.getRuleByName('vertical-align') is not None:
            self.errorMsg = self.errorMsg_verticalAlign;
            return False

        if rule.value == 'inline':
            if ruleSet.existNames('width,height,margin,margin-top,margin-bottom,float'):
                self.errorMsg = self.errorMsg_inline
                return False

        if rule.value.startswith('table-'):
            rules = ruleSet.getRules()
            for r in rules:
                if r.name.startswith('margin') or r.name == 'float':
                    self.errorMsg = self.errorMsg_tableXXX
                    return False
        return True 
