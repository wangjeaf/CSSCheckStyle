from Base import *
from helper import isHTMLTag

class FEDMustContainAuthorInfo(StyleSheetChecker):
    def __init__(self):
        self.id = 'add-author'
        self.errorMsg_author = 'should add @author in the head of "${file}"'
        self.errorMsg_empty = 'empty css file "${file}"'
        self.errorMsg = ''
        self.errorLevel = ERROR_LEVEL.ERROR

    def check(self, styleSheet, config):
        ruleSets = styleSheet.getRuleSets()
        if len(ruleSets) == 0:
            self.errorMsg = self.errorMsg_empty
            return False

        first = ruleSets[0]

        if styleSheet.getFile() != '' and first.comment.find('@author') == -1 and first.comment.find('@renren-inc.com') == -1:
            self.errorMsg = self.errorMsg_author
            return False
        return True 
