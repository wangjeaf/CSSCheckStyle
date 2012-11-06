from Base import *

class ShouldEnterWhenMultiSelectors(RuleSetChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'should "enter" in multi selector rule "${selector}"'

    def check(self, ruleSet):
        selector = ruleSet.roughSelector

        if selector.find(',') == -1:
            return True

        splited = selector.split(',')
        for i in range(1, len(splited)):
            s = splited[i]
            if s.find('\n') == -1:
                return False

        #if len(splited[len(splited) - 1].split('\n')) != 2:
        #    return False

        return True
