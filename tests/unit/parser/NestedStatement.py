from helper import *

def doTest():
    _withoutEnter()

def _withoutEnter():
    parser = CssParser("@keyframes 'blala' {10% {width: 100px;} 20% {width: 300px;}}@keyframes 'blala2' {10% {width: 200px;}}.test {_width : 100px;}")
    parser.doParse()
    ok(parser is not None, 'parser is not None')
    ok(parser.styleSheet is not None, 'parser.styleSheet is not None')
    equal(len(parser.styleSheet.getRuleSets()), 3, 'three rule set')

    styleSheet = parser.styleSheet
    first = styleSheet.getRuleSets()[0]
    ok(first.extra, 'keyframes is extra')
    equal(first.selector, "@keyframes 'blala'", 'it is @keyframes')
    equal(first.statement, '10% {width: 100px;} 20% {width: 300px;}', 'statement is ok')

    second = styleSheet.getRuleSets()[1]
    ok(second.extra, 'keyframes is extra')
    equal(second.selector, "@keyframes 'blala2'", 'it is @keyframes')
    equal(second.statement, '10% {width: 200px;}', 'statement is ok')

    rule = styleSheet.getRuleSets()[2]
    ok(not rule.extra, 'not extra')
    equal(rule.selector, '.test', 'selector is ok')
    equal(rule.getRuleByName('width').value, '100px', 'value is ok')
