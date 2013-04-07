#/usr/bin/python
#encoding=utf-8

'''
  0b11111111
    ||||||||
    ||||||||
    ||||||||--ie6 ---------|
    |||||||--ie7  ---------|
    ||||||--ie8   ---------| ALLIE
    |||||--ie9+   ---------|
    ||||
    ||||--opera ----|
    |||--safari ----|
    ||--ff      ----| STD
    |-- chrome  ----|
'''

ORIGIN = 0b00000000
CHROME = 0b10000000
FIREFOX= 0b01000000
SAFARI = 0b00100000
OPERA  = 0b00010000
STD    = CHROME | FIREFOX | SAFARI | OPERA

IE9PLUS= 0b00001000
IE8    = 0b00000100
IE7    = 0b00000010
IE6    = 0b00000001
ALLIE  = IE9PLUS | IE8 | IE7 | IE6

ALL    = 0b11111111