from EntityUtil import Cleaner
from Rule import Rule

class RuleSet():
    def __init__(self, selector, values, comment, styleSheet):
        self.extra = False
        self.roughSelector = selector
        self.roughValue = values
        self.roughComment = comment

        self.selector = Cleaner.clearSelector(selector)
        self.values = Cleaner.clearValues(values)
        self.comment = Cleaner.clearComment(comment)

        self.fixedSelector = ''
        self.fixedComment = ''

        self.styleSheet = styleSheet
        self._rules = []

        self.singleLineFlag = (len(self.roughValue.split('\n')) == 1)

    def compress(self):
        result = self.selector if self.fixedSelector == '' else self.fixedSelector
        result = result + '{'
        collector = []
        for rule in self._rules:
            collector.append(rule.compress())
        collected = ''.join(collector)
        if collected != '':
            collected = collected[0:-1]
        result = result + collected + '}'
        return result

    def getSingleLineFlag(self):
        return self.singleLineFlag

    def getStyleSheet(self):
        return self.styleSheet

    def addRuleByStr(self, selector, attr, value):
        self._rules.append(Rule(selector, attr, value, self))

    def indexOf(self, name):
        counter = 0
        for rule in self._rules:
            if rule.roughName.strip() == name:
                return counter
            counter = counter + 1
        return -1
    
    def existNames(self, name):
        if name.find(',') != -1:
            names = name.split(',')
        else:
            names = [name]
        for name in names:
            name = name.strip()
            for rule in self._rules:
                if rule.name == name:
                    return True
        return False

    def existRoughNames(self, name):
        if name.find(',') != -1:
            names = name.split(',')
        else:
            names = [name]
        for name in names:
            name = name.strip()
            for rule in self._rules:
                if rule.roughName.strip() == name:
                    return True
        return False

    def getRuleByStrippedName(self, name):
        for rule in self._rules:
            if rule.strippedName == name:
                return rule

    def getRuleByRoughName(self, name):
        for rule in self._rules:
            if rule.roughName == name:
                return rule

    def getRuleByName(self, name):
        for rule in self._rules:
            if rule.name == name:
                return rule

    def getRules(self):
        return self._rules

    def setRules(self, newRules):
        self._rules = newRules

    def __str__(self):
        return '%s {%s}' % (self.selector, self.roughValue)
