from helper import *

def doTest():
    _stylesheet()

def _stylesheet():
    styleSheet = StyleSheet('test.css')
    equal(styleSheet.getFile(), 'test.css', 'file name is ok')
    styleSheet.setFile('test2.css')
    equal(styleSheet.getFile(), 'test2.css', 'file nam changed')
    equal(styleSheet._file, styleSheet.getFile(), 'it is the same')

    equal(len(styleSheet.getRuleSets()), 0, 'no rule sets')
    equal(styleSheet.getRuleSetBySelector('.test'), None, 'can not find .test')

    styleSheet.addRuleSetByStr('.test', 'width:100px;height:100px', '/* fjdalkf */')
    equal(len(styleSheet.getRuleSets()), 1, 'one rule set')
    equal(styleSheet.getRuleSetBySelector('.test').selector, '.test', 'find .test')
    equal(styleSheet._ruleSets[0].comment, '/* fjdalkf */', 'comment is ok')
