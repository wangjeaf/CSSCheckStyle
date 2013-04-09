from helper import *

def doTest():
	equal(doRuleSetDetect('* html .test'), IE6, '* html')
	equal(doRuleSetDetect('* + html .test'), IE7, '* + html')
	equal(doRuleSetDetect('*:first-child+html .test'), IE7, '*:first-child+html .test')
	equal(doRuleSetDetect('html > body .test'), IE7 | IE8 | IE9PLUS, 'html > body')
	equal(doRuleSetDetect('html>/**/body .test'), IE8 | IE9PLUS, 'html>/**/body')
	equal(doRuleSetDetect('::-webkit-selection {}'), WEBKIT, '::-webkit-selection')
	equal(doRuleSetDetect('::-moz-selection {}'), FIREFOX, '::-moz-selection')
	equal(doRuleSetDetect('::-ms-selection {}'), IE9PLUS, '::-ms-selection')
	equal(doRuleSetDetect('::-o-selection {}'), OPERA, '::-o-selection')