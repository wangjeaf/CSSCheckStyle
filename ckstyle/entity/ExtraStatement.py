from .EntityUtil import Cleaner, ALL
from .RuleSet import RuleSet

class ExtraStatement(RuleSet):
    def __init__(self, operator, statement, comment, styleSheet = None):
        self.extra = True
        self.nested = False
        self.selector = self.operator = operator.strip()
        self.comment = comment
        self.statement = statement
        self.styleSheet = styleSheet

        self.fixedSelector = ''
        self.fixedStatement = ''

        self.browser = ALL

    def isImport(self):
        return self.operator == '@import'

    def rebase(self):
        self.fixedSelector = ''
        self.fixedStatement = ''
        
    def isOpmOperator(self):
        return self.operator.find('@-css-compiler') != -1

    def compress(self, browser = ALL):
        # do not export @-css-compiler to online 
        if self.isOpmOperator():
            return ''

        if not self.browser & browser:
            return ''
        msg = Cleaner.clean(self.statement)
        if not msg.endswith('}') and not msg.endswith(';'):
            msg = msg + ';'
        return msg

    def fixed(self, config):
        return self.statement.strip() if len(self.comment) == 0 else self.comment + '\n' + self.statement.strip()

    def __str__(self):
        return '%s' % self.statement
