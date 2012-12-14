from EntityUtil import Cleaner
import re
from RuleSet import RuleSet

replacer1 = re.compile('\s*{\s*')
replacer2 = re.compile('\s*:\s*')
replacer3 = re.compile('\s*;\s*}\s*')
replacer4 = re.compile('\s*;\s*')
replacer5 = re.compile('\s\s+')

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
        msg = self.statement.strip().replace('\r', '').replace('\n', '').replace(' ' * 4, ' ')
        msg = replacer1.sub('{', msg)
        msg = replacer2.sub(':', msg)
        msg = replacer3.sub('}', msg)
        msg = replacer4.sub(';', msg)
        msg = replacer5.sub(' ', msg)
        msg = msg.strip()
        if not msg.endswith('}') and not msg.endswith(';'):
            msg = msg + ';'
        return msg

    def fixed(self, config):
        return self.statement.strip()

    def __str__(self):
        return '%s' % self.statement
