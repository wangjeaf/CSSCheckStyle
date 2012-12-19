from helper import *

def doTest():
    _combine_should_not_make_mistake()
    _totally_same_ruleset()
    do_not_touch_background_position()

def _combine_should_not_make_mistake():
    css = '''.a {width:0px} 
.a, .b{width:1px}
.b{width:0px}'''

    expected = '''.a {
    width: 0;
}

.a,
.b {
    width: 1px;
}

.b {
    width: 0;
}'''
    fixer, msg = doFix(css, '')
    equal(msg, expected, 'do not make mistake when combine rulesets');

def do_not_touch_background_position():
    css = '''.a {background-position: 0 0} 
.test {width:1}
.b {background-position: 0 0} '''

    expected = '''.a {
    background-position: 0 0;
}

.test {
    width: 1;
}

.b {
    background-position: 0 0;
}'''
    fixer, msg = doFix(css, '')
    equal(msg, expected, 'do not combine background-position');

def _totally_same_ruleset():
    css = '''/*fdafda*/
.page-title {
   width: 100px;
   padding: 0px 1px;
}

.page-title {
   width: 100px;
   padding: 0px 1px;
}'''

    expected = '''/* fdafda */
.page-title {
    width: 100px;
    padding: 0 1px;
}'''
    fixer, msg = doFix(css, '')
    equal(msg, expected, 'it is the same ruleset');
