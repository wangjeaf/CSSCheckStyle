from Base import *
from helper import canBeCombined, isCss3PrefixProp

class FEDCombineInToOne(RuleSetChecker):
    def __init__(self):
        self.id = 'combine-into-one'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_rough = 'should combine "${small}" to "${big}" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet):
        rules = ruleSet.getRules()

        counter = {}
        for rule in rules:
            name = rule.name
            # -moz-border-radius, -o-border-radius is not for me
            if isCss3PrefixProp(name):
                continue

            bigger = canBeCombined(name)
            if bigger is not None:
                if counter.has_key(bigger):
                    counter[bigger].append(name)
                else:
                    counter[bigger] = [name]

        for name, value in counter.items():
            if len(value) > 1:
                self.errorMsg = self.errorMsg_rough.replace('${small}', ','.join(value)).replace('${big}', name)
                return False
        return True 
