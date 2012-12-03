from EntityUtil import Cleaner

class NestedStatement():
    def __init__(self, selector, statement, comments, styleSheet = None):
        self.extra = True
        self.selector = selector.strip()
        self.statement = statement.strip()
        self.roughStatement = statement
        self.comments = comments.strip()
        self.styleSheet = styleSheet

    def compress(self):
        return self.selector + '{' + self.statement.replace('\r', '').replace('\n', '').replace(' ' * 4, '').replace(': ', ':').replace(';}', '}') + '}'

    def fixed(self):
        spaces = ' ' * 4
        return self.selector + ' {\n' + self.roughStatement + '\n}'

    def __str__(self):
        return '%s' % self.statement
