from helper import *

def doTest():
    _go()

def _go():
    msg = doCssCompress('@media print{/* Hide the cursor when printing */.CodeMirror div.CodeMirror-cursor{visibility:hidden}}')
    equal(msg, '@media print{.CodeMirror div.CodeMirror-cursor{visibility:hidden}}', 'nested statement compress is ok')
