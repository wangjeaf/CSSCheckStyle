from Base import *
from helper import canBeCombined, isCss3PrefixProp
from combiners.CombinerFactory import doCombine

class FEDCombineInToOne(RuleSetChecker):
    def __init__(self):
        self.id = 'combine-into-one'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_rough = 'should combine "%s" to "%s" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        rules = ruleSet.getRules()

        counter = self._countCanBeCombined(rules)

        for name, value in counter.items():
            if len(value) > 1:
                self.errorMsg = self.errorMsg_rough % (','.join(value), name)
                return False
        return True 

    def fix(self, ruleSet, config):
        rules = ruleSet.getRules()
        counter = self._countCanBeCombined(rules, True)
        rules = self._combineAttrs(rules, counter)
        ruleSet.setRules(rules)

    def _countCanBeCombined(self, rules, forFix = False):
        counter = {}
        for rule in rules:
            name = rule.name
            # -moz-border-radius, -o-border-radius is not for me
            if isCss3PrefixProp(name):
                continue

            bigger = canBeCombined(name)
            if bigger is not None:
                if counter.has_key(bigger):
                    if forFix:
                        counter[bigger].append([name, rule.fixedName, rule.fixedValue])
                    else:
                        counter[bigger].append(name)
                else:
                    if forFix:
                        counter[bigger] = [[name, rule.fixedName, rule.fixedValue]]
                    else:
                        counter[bigger] = [name]
        return counter

    def _combineAttrs(self, rules, counter):
        originRules = rules
        for name, value in counter.items():
            combined, deleted, hasFather = doCombine(name, value)
            if combined == None:
                continue

            newRules = []
            for rule in originRules:
                # it is what i want
                if rule.fixedName == name:
                    rule.fixedValue = combined
                    newRules.append(rule)
                    continue
                # it is what i want to delete
                if rule.fixedName in deleted:
                    if not hasFather:
                        rule.reset(name, combined)
                        newRules.append(rule)
                        hasFather = True
                    continue
                newRules.append(rule)
            originRules = newRules
        return originRules
