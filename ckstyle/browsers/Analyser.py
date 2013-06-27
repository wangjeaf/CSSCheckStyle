#/usr/bin/python
#encoding=utf-8

from .BinaryRule import *

basic = {
	'ie6' : IE6,
	'ie7' : IE7,
	'ie8' : IE8,
	'ie9' : IE9PLUS,
	'ie10': IE9PLUS,
	'chrome' : CHROME,
	'firefox' : FIREFOX,
	'opera' : OPERA,
	'safari' : SAFARI,
	'std' : STD | NONEIE
}

mapping = {
	'ie' : ALLIE,
	'ie9plus' : IE9PLUS,
	'std' : STD | NONEIE
}

mapping.update(basic)

allBrowsers = ','.join([x for x in mapping.keys() if x != 'webkit' and x != 'ie9plus'])

def analyse(text):
	if not text or text == '' or text=='none' or text == 'false':
		return None
	if text == 'all':
		text = allBrowsers
	text = text.lower()
	splited = text.split(',')
	browsers = {}

	for browser in splited:
		if mapping.has_key(browser):
			# 不管如何选择，STD的总是要显示的
			browsers[browser] = mapping[browser] | STD
	return browsers

def whatIs(code):
	result = []
	for name, value in basic.items():
		if value & code:
			result.append(name)

	return ','.join(result)

if __name__ == '__main__':
	print(analyse('ie6,std'))
	print(whatIs(FIREFOX))