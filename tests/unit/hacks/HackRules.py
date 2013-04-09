from helper import *

def doTest():
	_ie()
	_other()
	#_ms()
	#_moz()
	#_o()

def _ie():
	equal(doRuleDetect('_width', 'fd'), IE6, '_width')
	equal(doRuleDetect('*width', 'fd'), IE6 | IE7, '*width')
	equal(doRuleDetect('+width', 'fd'), IE6 | IE7, '+width')
	equal(doRuleDetect('width', r'fd\9'), ALLIE, 'width\\9')
	equal(doRuleDetect('width', r'fd\0/'), IE8, 'width\\0/')
	equal(doRuleDetect('width', r'fd\0'), IE8 | IE9PLUS, 'width\\0')
	equal(doRuleDetect('zoom', '1'), ALLIE, 'zoom')
	equal(doRuleDetect('behavior', '1'), ALLIE, 'behavior')
	equal(doRuleDetect('filter', '1'), ALLIE, 'filter')
	equal(doRuleDetect('width', 'xxxx.Microsoft.AlphaImageLoader'), ALLIE, 'Microsoft')
	equal(doRuleDetect('width', 'expression()'), ALLIE, 'expression')

def _other():
	equal(doRuleDetect('-webkit-transition', 'fd'), WEBKIT, '-webkit-transition')
	equal(doRuleDetect('-moz-transition', 'fd'), FIREFOX, '-moz-transition')
	equal(doRuleDetect('-ms-transition', 'fd'), IE9PLUS, '-ms-transition')
	equal(doRuleDetect('-khtml-transition', 'fd'), ALLIE, '-khtml-transition')
	equal(doRuleDetect('-o-transition', 'fd'), OPERA, '-o-transition')

	equal(doRuleDetect('background', '-webkit-linear-gradient()'), WEBKIT, '-webkit-gradient')
	equal(doRuleDetect('background', '-moz-linear-gradient()'), FIREFOX, '-moz-gradient')
	equal(doRuleDetect('background', '-ms-linear-gradient()'), IE9PLUS, '-ms-gradient')
	equal(doRuleDetect('background', '-khtml-linear-gradient()'), ALLIE, '-khtml-gradient')
	equal(doRuleDetect('background', '-o-linear-gradient()'), OPERA, '-o-gradient')