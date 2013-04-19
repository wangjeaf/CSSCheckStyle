#/usr/bin/python
#encoding=utf-8

'''
  0b111111111
    |||||||||
    |||||||||
    |||||||||--ie6 ---------|
    ||||||||--ie7  ---------|
    |||||||--ie8   ---------| ALLIE
    ||||||--ie9+   ---------|
    |||||
    |||||--opera
    ||||--safari   ---------|
    |||--firefox            | WEBKIT
    ||-- chrome    ---------|
    |-- STD
'''

ORIGIN = 0b000000000

STD    = 0b100000000
CHROME = 0b010000000
FIREFOX= 0b001000000
SAFARI = 0b000100000
OPERA  = 0b000010000

WEBKIT = CHROME | SAFARI 

NONEIE = CHROME | SAFARI | OPERA | FIREFOX

IE9PLUS= 0b000001000
IE8    = 0b000000100
IE7    = 0b000000010
IE6    = 0b000000001
ALLIE  = IE9PLUS | IE8 | IE7 | IE6

NOIE6  = IE9PLUS | IE8 | IE7 | NONEIE
NOIE67 = IE9PLUS | IE8 | NONEIE
NOIE678= IE9PLUS | NONEIE
NONE   = 0b000000000
ALL    = 0b111111111