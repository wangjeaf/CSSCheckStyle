from EntityUtil import Cleaner
from RuleSet import RuleSet

class ExtraStatement(RuleSet):
    def __init__(self, operator, statement, styleSheet = None):
        self.extra = True
        self.operator = operator.strip()
        self.statement = statement
        self.styleSheet = styleSheet

    def isImport(self):
        return self.operator == '@import'

    def isOpmOperator(self):
        return self.operator.find('@-css-compiler') != -1

    def __str__(self):
        return '%s' % self.statement
