#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDCommentLengthLessThan80(RuleSetChecker):

    '''{
        "summary":"注释不能超过80个字符",
        "desc":"注释长度不能超过80个字符，40个汉字，如果超出，则应该要换行~"
    }'''

    def __init__(self):
        self.id = 'comment-length'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'comment for "${selector}" length should less than 80 per line'

    def check(self, ruleSet, config):
        comment = ruleSet.roughComment
        if len(comment) == 0:
            return True

        cs = comment.split('\n')
        for c in cs:
            if len(c.strip()) > 80:
                return False
        return True 
