#/usr/bin/python
#encoding=utf-8
from BinaryRule import *
import re

# http://www.swordair.com/tools/css-hack-table/
# big table

# some hacks
RULE_HACKS = [
    [r'^_',                     1,  IE6],
    [r'^\+',                    1,  IE6 | IE7],
    [r'^\*',                    1,  IE6 | IE7],
    [r'.*\\9',                  2,  ALLIE],
    [r'.*\\0/',                 2,  IE8],
    [r'.*\\0',                  2,  IE8 | IE9PLUS],

    [r'zoom|behavior|filter',   1,  ALLIE],

    [r'.*Microsoft',            2,  ALLIE],
    [r'^expression',            2,  ALLIE],

    [r'^\-webkit\-',            1,  WEBKIT],
    [r'^\-webkit\-',            2,  WEBKIT],
    [r'^\-moz\-',               1,  FIREFOX],
    [r'^\-moz\-',               2,  FIREFOX],
    [r'^\-ms\-',                1,  IE9PLUS],
    [r'^\-ms\-',                2,  IE9PLUS],
    [r'^\-khtml\-',             1,  ALLIE],
    [r'^\-khtml\-',             2,  ALLIE],
    [r'^\-o\-',                 1,  OPERA],
    [r'^\-o\-',                 2,  OPERA]
]

# some hacks
RULESET_HACKS = [
    [r'\*html',                 IE6],
    [r'\*\+html',               IE7],
    [r'\*:first\-child\+html',  IE7],
    [r'html>body',              IE7 | IE8 | IE9PLUS],
    [r'html>/\*\*/body',        IE8 | IE9PLUS],
    [r'.*\-webkit\-',           WEBKIT],
    [r'.*\-moz\-',              FIREFOX],
    [r'.*\-ms\-',               IE9PLUS],
    [r'.*\-o\-',                OPERA]
]

# some hacks
EXTRA_HACKS = [
    [r'@\-webkit\-keyframes',   WEBKIT],
    [r'@\-moz\-keyframes',      FIREFOX],
    [r'@\-ms\-keyframes',       IE9PLUS],
    [r'@\-o\-keyframes',        OPERA],
    [r'@keyframes',             NONEIE | IE9PLUS],

    [r'@\-moz\-document',       FIREFOX],
    [r'@mediascreenand\(\-webkit\-min\-device\-pixel\-ratio:0\)',  WEBKIT],
    [r'@mediascreenand\(max\-device\-width:480px\)',               WEBKIT],
    [r'@mediaalland\(\-webkit\-min\-device\-pixel\-ratio:10000\),notalland\(\-webkit\-min\-device\-pixel\-ratio:0\)',  OPERA]
]

def doRuleDetect(name, value):
    name = name.strip().replace(' ', '')
    value = value.strip().replace(' ', '')
    for hack in RULE_HACKS:
        pattern = re.compile(hack[0])
        match = pattern.match(name if hack[1] == 1 else value)
        if match:
            return hack[2]
    return STD

def doRuleSetDetect(selector):
    selector = selector.strip().replace(' ', '')
    for hack in RULESET_HACKS:
        pattern = re.compile(hack[0])
        match = pattern.match(selector)
        if match:
            return hack[1]
    return STD

def doExtraDetect(selector):
    selector = selector.strip().replace(' ', '')
    for hack in EXTRA_HACKS:
        pattern = re.compile(hack[0])
        match = pattern.match(selector)
        if match:
            return hack[1]
    return STD

if __name__ == '__main__':
    print bin(doExtraDetect('@media screen and (max-device-width: 480px)'))
    print bin(doExtraDetect('@media screen and (-webkit-min-device-pixel-ratio:0)'))
    print bin(doExtraDetect('@media all and (-webkit-min-device-pixel-ratio:10000), not all and (-webkit-min-device-pixel-ratio:0)'))