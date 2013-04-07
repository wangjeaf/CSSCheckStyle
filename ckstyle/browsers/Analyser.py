#/usr/bin/python
#encoding=utf-8

from BinaryRule import *
mapping = {
	'ie6' : IE6,
	'ie7' : IE7,
	'ie8' : IE8,
	'ie9' : IE9PLUS,
	'std' : STD
}

def analyse(text):
	if not text or text == '' or text=='none' or text == 'false':
		return None

	text = text.lower()
	splited = text.split(',')
	browsers = {}

	for browser in splited:
		if mapping.has_key(browser):
			# 不管如何选择，STD的总是要显示的
			browsers[browser] = mapping[browser] | STD
	return browsers

if __name__ == '__main__':
	print analyse('ie6,std')