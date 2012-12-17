from EntityUtil import Cleaner

class Rule():
    def __init__(self, selector, name, value, ruleSet):
        self.roughName = name
        self.roughValue = value
        self.roughSelector = selector

        self.name = Cleaner.clearName(name)
        self.value = Cleaner.clearValue(value)
        self.selector = Cleaner.clearSelector(selector)

        self.strippedName = name.strip()
        self.strippedValue = value.strip()
        self.strippedSelector = selector.strip()

        self.fixedName = ''
        self.fixedValue = ''

        self.ruleSet = ruleSet

    def reset(self, name, value):
        self.roughName = self.name = self.strippedName = self.fixedName = name
        self.roughValue = self.value = self.strippedValue = self.fixedValue = value

    def compress(self):
        name = self.name if self.fixedName == '' else self.fixedName.strip()
        value = self.value if self.fixedValue == '' else self.fixedValue.strip()
        return name + ':' + Cleaner.clean(value) + ';'

    def fixed(self):
        name = self.name if self.fixedName == '' else self.fixedName
        value = self.value if self.fixedValue == '' else self.fixedValue
        return name + ': ' + Cleaner.clean(value) + ';'

    def getRuleSet(self):
        return self.ruleSet

    def __str__(self):
        return ' roughName: %s\n name: %s\n roughValue: %s\n value: %s\n' % (self.roughName, self.name, self.roughValue, self.value)
