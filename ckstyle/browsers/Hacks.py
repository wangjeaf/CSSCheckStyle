#/usr/bin/python
#encoding=utf-8
from .BinaryRule import *
import re


#SCRIPT AUTO-GENERATOR
#execute on http://www.w3schools.com/cssref/css3_browsersupport.asp
#
#var trs = document.querySelectorAll('table.reference tr');
#var contents = [], l = trs.length, tr, tds, ie, ff, ch, sa, op;
#
#for(var i = 0; i < l; i++) {
#     tr = trs[i];
#     tds = tr.querySelectorAll('td');
#     if (tds.length == 0) {
#        continue
#     }
#     prop = tds[0].innerHTML;
#     if (prop.indexOf('<') != -1) {
#        prop = tds[0].firstChild.innerHTML
#     }
#     if (tds[1].className == 'bsNoIE') {
#        ie = 0;
#     } else if (tds[1].className == 'bsIE') {
#        ie = tds[1].innerHTML || 9
#     } else if (tds[1].className == 'bsPreIE') {
#        ie = tds[1].innerHTML || 9
#     }
#     //if (prop == 'text-emphasis') console.log(prop, ie);
#     
#     if (tds[2].className == 'bsNoFirefox') {
#        ff = 0;
#     } else if (tds[2].className == 'bsFirefox') {
#        ff = tds[2].innerHTML || 1
#     } else if (tds[2].className == 'bsPreFirefox') {
#        ff = 1
#     } else {
#        
#     }
#     
#     if (tds[3].className == 'bsNoChrome') {
#        ch = 0;
#     } else if (tds[3].className == 'bsChrome') {
#        ch = tds[3].innerHTML || 1
#     } else if (tds[3].className == 'bsPreChrome') {
#        ch = 1
#     } else {
#     }
#     
#     if (tds[4].className == 'bsNoSafari') {
#        sa = 0;
#     } else if (tds[4].className == 'bsSafari') {
#        sa = tds[4].innerHTML || 1
#     } else if (tds[4].className == 'bsPreSafari') {
#        sa = 1
#     } else {
#     }
#     
#     if (tds[5].className == 'bsNoOpera') {
#        op = 0;
#     } else if (tds[5].className == 'bsOpera') {
#        op = tds[5].innerHTML || 1
#     } else if (tds[5].className == 'bsPreOpera') {
#        op = 1
#     } else {
#     }
#     final = []
#     if (ie) {
#         if (ie <=6) {
#             final.push('ALLIE')
#         } else if (ie == 7) {
#             final.push('IE7 | IE8 | IE9PLUS')
#         } else if (ie == 8) {
#            final.push('IE8 | IE9PLUS')
#         } else if (!!ie){
#            final.push('IE9PLUS')
#         }
#    }
#     if (!!ff) {
#        final.push('FIREFOX')
#     }
#     if (!!ch) {
#        final.push('CHROME')
#    }
#    if (!!sa) {
#        final.push('SAFARI')
#    }
#    if (!!op) {
#        final.push('OPERA');
#    }
#    result = final.join(' | ');
#    if (!result) {
#        result = 'NONE'
#    }    
#    contents.push('[r\'^' + prop.replace(/\-/g, '\\-') + '\', 1, ' + result + '],');
#}
#console.log(contents.join('\n'));

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

    [r'.*(m|M)icrosoft',        2,  ALLIE],
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
    [r'^\-o\-',                 2,  OPERA],

    # auto generate by script AUTO-GENERATOR .
    [r'^alignment\-adjust', 1, NONE],
    [r'^alignment\-baseline', 1, NONE],
    [r'^animation', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-name', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-duration', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-timing\-function', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-delay', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-iteration\-count', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-direction', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^animation\-play\-state', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^appearance', 1, FIREFOX | CHROME | SAFARI],
    [r'^backface\-visibility', 1, IE9PLUS | FIREFOX | CHROME | SAFARI],
    [r'^background\-clip', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^background\-origin', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^background\-size', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^baseline\-shift', 1, NONE],
    [r'^bookmark\-label', 1, NONE],
    [r'^bookmark\-level', 1, NONE],
    [r'^bookmark\-target', 1, NONE],
    [r'^border\-bottom\-left\-radius', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^border\-bottom\-right\-radius', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^border\-image', 1, FIREFOX | CHROME | SAFARI | OPERA],
    [r'^border\-image\-outset', 1, NONE],
    [r'^border\-image\-repeat', 1, NONE],
    [r'^border\-image\-slice', 1, NONE],
    [r'^border\-image\-source', 1, NONE],
    [r'^border\-image\-width', 1, NONE],
    [r'^border\-radius', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^border\-top\-left\-radius', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^border\-top\-right\-radius', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^box\-decoration\-break', 1, NONE],
    [r'^box\-align', 1, FIREFOX | CHROME | SAFARI],
    [r'^box\-direction', 1, FIREFOX | CHROME | SAFARI],
    [r'^box\-flex', 1, FIREFOX | CHROME | SAFARI | OPERA],
    [r'^box\-flex\-group', 1, NONE],
    [r'^box\-lines', 1, NONE],
    [r'^box\-ordinal\-group', 1, FIREFOX | CHROME | SAFARI],
    [r'^box\-orient', 1, FIREFOX | CHROME | SAFARI],
    [r'^box\-pack', 1, FIREFOX | CHROME | SAFARI],
    [r'^box\-shadow', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^box\-sizing', 1, IE8 | IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^color\-profile', 1, NONE],
    [r'^column\-fill', 1, NONE],
    [r'^column\-gap', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^column\-rule', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^column\-rule\-color', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^column\-rule\-style', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^column\-rule\-width', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^column\-span', 1, IE9PLUS | CHROME | SAFARI | OPERA],
    [r'^column\-width', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^columns', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^column\-count', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^crop', 1, NONE],
    [r'^dominant\-baseline', 1, NONE],
    [r'^drop\-initial\-after\-adjust', 1, NONE],
    [r'^drop\-initial\-after\-align', 1, NONE],
    [r'^drop\-initial\-before\-adjust', 1, NONE],
    [r'^drop\-initial\-before\-align', 1, NONE],
    [r'^drop\-initial\-size', 1, NONE],
    [r'^drop\-initial\-value', 1, NONE],
    [r'^fit', 1, NONE],
    [r'^fit\-position', 1, NONE],
    [r'^float\-offset', 1, NONE],
    [r'^font\-size\-adjust', 1, FIREFOX],
    [r'^font\-stretch', 1, NONE],
    [r'^grid\-columns', 1, NONE],
    [r'^grid\-rows', 1, NONE],
    [r'^hanging\-punctuation', 1, NONE],
    [r'^hyphenate\-after', 1, NONE],
    [r'^hyphenate\-before', 1, NONE],
    [r'^hyphenate\-characters', 1, NONE],
    [r'^hyphenate\-lines', 1, NONE],
    [r'^hyphenate\-resource', 1, NONE],
    [r'^hyphens', 1, NONE],
    [r'^icon', 1, NONE],
    [r'^image\-orientation', 1, NONE],
    [r'^image\-resolution', 1, NONE],
    [r'^inline\-box\-align', 1, NONE],
    [r'^line\-stacking', 1, NONE],
    [r'^line\-stacking\-ruby', 1, NONE],
    [r'^line\-stacking\-shift', 1, NONE],
    [r'^line\-stacking\-strategy', 1, NONE],
    [r'^mark', 1, NONE],
    [r'^mark\-after', 1, NONE],
    [r'^mark\-before', 1, NONE],
    [r'^marks', 1, NONE],
    [r'^marquee\-direction', 1, CHROME | SAFARI],
    [r'^marquee\-play\-count', 1, CHROME | SAFARI],
    [r'^marquee\-speed', 1, CHROME | SAFARI],
    [r'^marquee\-style', 1, CHROME | SAFARI],
    [r'^move\-to', 1, NONE],
    [r'^nav\-down', 1, OPERA],
    [r'^nav\-index', 1, OPERA],
    [r'^nav\-left', 1, OPERA],
    [r'^nav\-right', 1, OPERA],
    [r'^nav\-up', 1, OPERA],
    [r'^opacity', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^outline\-offset', 1, FIREFOX | CHROME | SAFARI | OPERA],
    [r'^overflow\-style', 1, NONE],
    [r'^overflow\-x', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^overflow\-y', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^page', 1, NONE],
    [r'^page\-policy', 1, NONE],
    [r'^perspective', 1, CHROME | SAFARI],
    [r'^perspective\-origin', 1, CHROME | SAFARI],
    [r'^punctuation\-trim', 1, NONE],
    [r'^rendering\-intent', 1, NONE],
    [r'^resize', 1, FIREFOX | CHROME | SAFARI],
    [r'^rest', 1, NONE],
    [r'^rest\-after', 1, NONE],
    [r'^rest\-before', 1, NONE],
    [r'^rotation', 1, NONE],
    [r'^rotation\-point', 1, NONE],
    [r'^ruby\-align', 1, IE9PLUS],
    [r'^ruby\-overhang', 1, IE9PLUS],
    [r'^ruby\-position', 1, IE9PLUS],
    [r'^ruby\-span', 1, NONE],
    [r'^size', 1, NONE],
    [r'^string\-set', 1, NONE],
    [r'^target', 1, NONE],
    [r'^target\-name', 1, NONE],
    [r'^target\-new', 1, NONE],
    [r'^target\-position', 1, NONE],
    [r'^text\-align\-last', 1, NONE],
    [r'^text\-emphasis', 1, NONE],
    [r'^text\-height', 1, NONE],
    [r'^text\-justify', 1, ALLIE],
    [r'^text\-outline', 1, NONE],
    [r'^text\-overflow', 1, ALLIE | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^text\-shadow', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^text\-wrap', 1, NONE],
    [r'^transform', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^transform\-origin', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^transform\-style', 1, CHROME | SAFARI],
    [r'^transition', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^transition\-property', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^transition\-duration', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^transition\-timing\-function', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^transition\-delay', 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [r'^word\-break', 1, ALLIE | FIREFOX | CHROME | SAFARI],
    [r'^word\-wrap', 1, ALLIE | FIREFOX | CHROME | SAFARI | OPERA]
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
    [r'@font\-face',           IE9PLUS | NONEIE],

    [r'@\-moz\-document',       FIREFOX],
    [r'@mediascreenand\(\-webkit\-min\-device\-pixel\-ratio:0\)',  WEBKIT],
    [r'@mediascreenand\(max\-device\-width:480px\)',               WEBKIT],
    [r'@mediaalland\(\-webkit\-min\-device\-pixel\-ratio:10000\),notalland\(\-webkit\-min\-device\-pixel\-ratio:0\)',  OPERA]
]

def doRuleDetect(name, value):
    name = name.strip().replace(' ', '')
    value = value.strip().replace(' ', '')

    for hack in RULE_HACKS:
        if hack[1] == 1 and name == hack[0]:
           return hack[2]
        pattern = re.compile(hack[0])
        match = pattern.match(name if hack[1] == 1 else value)
        if match:
            #print name, value, bin(hack[2])
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
    print(bin(doExtraDetect('@media screen and (max-device-width: 480px)')))
    print(bin(doExtraDetect('@media screen and (-webkit-min-device-pixel-ratio:0)')))
    print(bin(doExtraDetect('@media all and (-webkit-min-device-pixel-ratio:10000), not all and (-webkit-min-device-pixel-ratio:0)')))