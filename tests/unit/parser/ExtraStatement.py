from helper import *

def doTest():
    _withEnter()
    _withoutEnter()

def _withoutEnter():
    parser = CssParser('@import url(xxxx);@charset utf-8;.test {_width : 100px;}')
    parser.doParse()
    ok(parser is not None, 'parser is not None')
    ok(parser.styleSheet is not None, 'parser.styleSheet is not None')
    equal(len(parser.styleSheet.getRuleSets()), 3, 'three rule set')

    styleSheet = parser.styleSheet
    importer = styleSheet.getRuleSets()[0]
    ok(importer.extra, 'import is extra')
    ok(importer.isImport(), 'it is import')
    equal(importer.operator, '@import', 'it is @import')
    equal(importer.statement, '@import url(xxxx);', 'statement is ok')

    charset = styleSheet.getRuleSets()[1]
    ok(charset.extra, 'charset is extra')
    ok(not charset.isImport(), 'it is not import')
    equal(charset.operator, '@charset', 'it is @charset')
    equal(charset.statement, '@charset utf-8;', 'statement is ok')

    rule = styleSheet.getRuleSets()[2]
    ok(not rule.extra, 'not extra')
    equal(rule.selector, '.test', 'selector is ok')
    equal(rule.getRuleByName('width').value, '100px', 'value is ok')

def _withEnter():
    parser = CssParser('@import url(xxxx);\n@charset utf-8;\n.test {_width : 100px;}')
    parser.doParse()
    ok(parser is not None, 'parser is not None')
    ok(parser.styleSheet is not None, 'parser.styleSheet is not None')
    equal(len(parser.styleSheet.getRuleSets()), 3, 'three rule set')

    styleSheet = parser.styleSheet
    importer = styleSheet.getRuleSets()[0]
    ok(importer.extra, 'import is extra')
    ok(importer.isImport(), 'it is import')
    equal(importer.operator, '@import', 'it is @import')
    equal(importer.statement, '@import url(xxxx);', 'statement is ok')

    charset = styleSheet.getRuleSets()[1]
    ok(charset.extra, 'charset is extra')
    ok(not charset.isImport(), 'it is not import')
    equal(charset.operator, '@charset', 'it is @charset')
    equal(charset.statement, '@charset utf-8;', 'statement is ok')

    rule = styleSheet.getRuleSets()[2]
    ok(not rule.extra, 'not extra')
    equal(rule.selector, '.test', 'selector is ok')
    equal(rule.getRuleByName('width').value, '100px', 'value is ok')
