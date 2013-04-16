from .EntityUtil import Cleaner, ALL

class NestedStatement():
    def __init__(self, selector, statement, comments, styleSheet = None):
        self.extra = True
        self.nested = True
        self.selector = selector.strip()
        self.statement = statement.strip()
        self.roughStatement = statement
        self.comments = comments.strip()
        self.styleSheet = styleSheet

        self.fixedSelector = ''
        self.fixedStatement = ''

        self.browser = ALL
        self.toBeUsed = {}

    def rebase(self):
        self.fixedSelector = ''
        self.fixedStatement = ''
        
    def compress(self, browser = ALL):
        if not self.browser & browser:
            return ''
        return self.fixedSelector + self._compressedStatement()

    def fixed(self, config):
        return self.fixedSelector + ' {\n    ' + '\n    '.join(self.fixedStatement.split('\n')) + '\n}'

    def _compressedStatement(self):
        return '{' + Cleaner.clean(self.fixedStatement) + '}'

    def __str__(self):
        return '%s' % self.statement
