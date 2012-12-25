from EntityUtil import Cleaner
from RuleSet import RuleSet

class ExtraStatement(RuleSet):
    def __init__(self, operator, statement, comment, styleSheet = None):
        self.extra = True
        self.operator = operator.strip()
        self.comment = comment
        self.statement = statement
        self.styleSheet = styleSheet

    def isImport(self):
        return self.operator == '@import'

    def isOpmOperator(self):
        return self.operator.find('@-css-compiler') != -1

    def compress(self):
        msg = Cleaner.clean(self.statement)
        if not msg.endswith('}') and not msg.endswith(';'):
            msg = msg + ';'
        return msg

    def fixed(self, config):
        return self.statement.strip() if len(self.comment) == 0 else self.comment + '\n' + self.statement.strip()

    def __str__(self):
        return '%s' % self.statement
