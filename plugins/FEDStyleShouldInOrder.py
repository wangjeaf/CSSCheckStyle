from Base import *

class FEDStyleShouldInOrder(RuleSetChecker):
    def __init__(self):
        self.id = 'keep-in-order'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'should attributes keep in display/box/text/other/css3 order "${selector}"'

    def check(self, rule):
        return True 
