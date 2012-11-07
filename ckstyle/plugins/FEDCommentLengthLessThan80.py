from Base import *

class FEDCommentLengthLessThan80(RuleSetChecker):
    def __init__(self):
        self.id = 'comment-length'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'comment for "${selector}" length should less than 80 per line'

    def check(self, ruleSet):
        comment = ruleSet.roughComment
        if len(comment) == 0:
            return True

        cs = comment.split('\n')
        for c in cs:
            if len(c.strip()) > 80:
                return False
        return True 
