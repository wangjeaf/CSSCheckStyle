from EntityUtil import Cleaner

class Rule():
    def __init__(self, selector, name, value, ruleSet):
        self.roughName = name
        self.roughValue = value
        self.roughSelector = selector

        self.name = Cleaner.clearName(name)
        self.value = Cleaner.clearValue(value)
        self.selector = Cleaner.clearSelector(selector)

        self.ruleSet = ruleSet

    def getRuleSet(self):
        return self.ruleSet

    def __str__(self):
        return ' roughName: %s\n name: %s\n roughValue: %s\n value: %s\n' % (self.roughName, self.name, self.roughValue, self.value)
