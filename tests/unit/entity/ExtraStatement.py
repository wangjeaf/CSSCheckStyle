from helper import *

def doTest():
    _basic()
    _opm()
    _other()

def _basic():
    stmt = ExtraStatement('@import', '@import url("fjdaslkjfdsa")', None)
    ok(stmt.extra, '@import is extra statement')
    equal(stmt.operator, '@import', 'operator is @important')
    equal(stmt.statement, '@import url("fjdaslkjfdsa")', 'statement is ok')
    equal(stmt.styleSheet, None, 'no style sheet')
    ok(stmt.isImport(), 'yes, it is import statement')
    ok(not stmt.isOpmOperator(), 'no, it is not opm operator')

def _opm():
    stmt = ExtraStatement('@-css-compiler-xxx', '@-css-compiler-xxx fdjafdjafda;', None)
    ok(stmt.isOpmOperator(), 'yes, it is opm operator')

    stmt = ExtraStatement('@-css-compiler-xxx', '@-css-compiler-xxx fdjafdjafda;', None)
    ok(stmt.isOpmOperator(), 'yes, it is opm operator')

def _other():
    stmt = ExtraStatement('@namspace', '@namspace fdjafdjafda;', None)
    ok(not stmt.isOpmOperator(), 'no, it is not opm operator')
    ok(not stmt.isImport(), 'no, it is not import')

    stmt = ExtraStatement('@charset', '@charset utf-8;', None)
    ok(not stmt.isOpmOperator(), 'no, it is not opm operator')
    ok(not stmt.isImport(), 'no, it is not import')
