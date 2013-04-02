#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import canBeCombined, isCss3PrefixProp, containsHack
from combiners.CombinerFactory import doCombine

class FEDCombineInToOne(RuleSetChecker):
    
    '''{
        "summary":"将多个子样式合并",
        "desc":"有的子样式可以合并为总样式，包括
            <code>margin</code> <code>padding</code> <code>font</code> <code>background</code> <code>border</code>
            等，合并以后可以获得更好的执行效率和压缩效果，<br/>
            例如：<br/>
            <code>.test {margin:4px; margin-right:0;}</code><br/>
            <code>==></code><br/>
            <code>.test{margin:4px 0 4px 4px}</code><br/>
        "
    }'''

    def __init__(self):
        self.id = 'combine-into-one'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_rough = 'should combine "%s" to "%s" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        rules = ruleSet.getRules()

        counter = self._countCanBeCombined(rules)

        for name, value in counter.items():
            if name == 'font' and len(value) > 2 or name != 'font' and len(value) > 1:
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
            if rule.name != rule.strippedName:
                continue
            # do not do any hack combine
            if containsHack(rule):
                continue
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
                if containsHack(rule):
                    newRules.append(rule)
                    continue
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
