from RuleSet import RuleSet

class StyleSheet():
    def __init__(self, fileName = ''):
        self._ruleSets = [];
        self._file = fileName

    def addRuleSetByStr(self, selector, attrs, comment):
        self._ruleSets.append(RuleSet(selector, attrs, comment, self))

    def setFile(self, fileName):
        self._file = fileName

    def getFile(self):
        return self._file

    def getRuleSets(self):
        return self._ruleSets

    def getRuleSetBySelector(self, selector):
        for ruleSet in self._ruleSets:
            if ruleSet.selector == selector:
                return ruleSet
