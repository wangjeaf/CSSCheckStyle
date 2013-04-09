from helper import *

def doTest():
	_standard_hack()
	_keyframes()

def _standard_hack():
    equal(doExtraDetect('@media screen and (max-device-width: 480px)'.replace(' ', '')), WEBKIT, 'webkit mobile hack is ok')
    equal(doExtraDetect('@media screen and (-webkit-min-device-pixel-ratio:0)'.replace(' ', '')), WEBKIT, 'webkit hack is ok')
    equal(doExtraDetect('@media all and (-webkit-min-device-pixel-ratio:10000), not all and (-webkit-min-device-pixel-ratio:0)'.replace(' ', '')), OPERA, 'opera hack is ok')

def _keyframes():
	equal(doExtraDetect('@keyframes fda'), NONEIE | IE9PLUS, '@keyframes')
	equal(doExtraDetect('@-webkit-keyframes fda'), WEBKIT, '@-webkit-keyframes')
	equal(doExtraDetect('@-moz-keyframes fda'), FIREFOX, '@-moz-keyframes')
	equal(doExtraDetect('@-ms-keyframes fda'), IE9PLUS, '@-ms-keyframes')
	equal(doExtraDetect('@-o-keyframes fda'), OPERA, '@-o-keyframes')