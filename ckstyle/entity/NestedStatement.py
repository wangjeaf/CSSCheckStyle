from EntityUtil import Cleaner

class NestedStatement():
    def __init__(self, selector, statement, comments, styleSheet = None):
        self.extra = True
        self.selector = selector.strip()
        self.statement = statement.strip()
        self.comments = comments.strip()
        self.styleSheet = styleSheet

    def compress(self):
        return self.selector + '{' + self.statement.replace('\n', '').replace(' ' * 4, '') + '}'

    def __str__(self):
        return '%s' % self.statement
