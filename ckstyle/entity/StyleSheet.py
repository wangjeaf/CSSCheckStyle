from RuleSet import RuleSet
from ExtraStatement import ExtraStatement
from NestedStatement import NestedStatement

class StyleSheet():
    def __init__(self, fileName = ''):
        self._ruleSets = [];
        self._file = fileName

    def addRuleSetByStr(self, selector, attrs, comment):
        self._ruleSets.append(RuleSet(selector, attrs, comment, self))

    def addExtraStatement(self, operator, statement, comment):
        self._ruleSets.append(ExtraStatement(operator, statement, comment, self))

    def addNestedRuleSet(self, selector, attrs, comment):
        self._ruleSets.append(NestedStatement(selector, attrs, comment, self))

    def setFile(self, fileName):
        self._file = fileName

    def getFile(self):
        return self._file

    def getRuleSets(self):
        return self._ruleSets

    def removeRuleSetByIndex(self, index):
        self._ruleSets[index] = None

    def removeRuleSet(self, ruleSet):
        newRuleSets = []
        for x in self._ruleSets:
            if x == ruleSet:
                continue
            newRuleSets.append(x)
        self._ruleSets = newRuleSets

    def clean(self):
        newRuleSets = []
        for x in self._ruleSets:
            if x is None:
                continue
            newRuleSets.append(x)
        self._ruleSets = newRuleSets

    def getRuleSetBySelector(self, selector):
        for ruleSet in self._ruleSets:
            if ruleSet.selector == selector:
                return ruleSet

    def compress(self):
        result = []
        for ruleSet in self._ruleSets:
            result.append(ruleSet.compress())
        return ''.join(result)

    def fixed(self, config):
        result = []
        for ruleSet in self._ruleSets:
            result.append(ruleSet.fixed(config))
        return '\n\n'.join(result)
