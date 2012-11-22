from EntityUtil import Cleaner
from Rule import Rule

class ExtraStatement():
    def __init__(self, operator, statement, styleSheet = None):
        self.operator = operator.strip()
        self.statement = statement
        self.styleSheet = styleSheet

    def isImport(self):
        return self.operator == '@import'

    def isOpmOperator(self):
        return self.operator.find('@-css-compiler') != -1

    def __str__(self):
        return '%s' % self.statement
