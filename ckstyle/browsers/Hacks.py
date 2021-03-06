#/usr/bin/python
#encoding=utf-8
from BinaryRule import *
import re

# http://www.swordair.com/tools/css-hack-table/
# big table

# some hacks
RULE_HACKS = [
    [re.compile(r'^_'),                     1,  IE6],
    [re.compile(r'^\+'),                    1,  IE6 | IE7],
    [re.compile(r'^\*'),                    1,  IE6 | IE7],
    [re.compile(r'.*\\9'),                  2,  ALLIE],
    [re.compile(r'.*\\0/'),                 2,  IE8],
    [re.compile(r'.*\\0'),                  2,  IE8 | IE9PLUS],
    [re.compile(r'zoom|behavior|filter'),   1,  ALLIE],
    [re.compile(r'.*(m|M)icrosoft'),        2,  ALLIE],
    [re.compile(r'^expression'),            2,  ALLIE],
    [re.compile(r'^\-webkit\-'),            1,  WEBKIT],
    [re.compile(r'^\-webkit\-'),            2,  WEBKIT],
    [re.compile(r'^\-moz\-'),               1,  FIREFOX],
    [re.compile(r'^\-moz\-'),               2,  FIREFOX],
    [re.compile(r'^\-ms\-'),                1,  IE9PLUS],
    [re.compile(r'^\-ms\-'),                2,  IE9PLUS],
    [re.compile(r'^\-khtml\-'),             1,  ALLIE],
    [re.compile(r'^\-khtml\-'),             2,  ALLIE],
    [re.compile(r'^\-o\-'),                 1,  OPERA],
    [re.compile(r'^\-o\-'),                 2,  OPERA],

    # auto generated by script AUTO-GENERATOR-1 .
    [re.compile(r'^alignment\-adjust'), 1, NONE],
    [re.compile(r'^alignment\-baseline'), 1, NONE],
    [re.compile(r'^animation'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-name'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-duration'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-timing\-function'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-delay'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-iteration\-count'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-direction'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^animation\-play\-state'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^appearance'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^backface\-visibility'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI],
    [re.compile(r'^background\-clip'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^background\-origin'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^background\-size'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^baseline\-shift'), 1, NONE],
    [re.compile(r'^bookmark\-label'), 1, NONE],
    [re.compile(r'^bookmark\-level'), 1, NONE],
    [re.compile(r'^bookmark\-target'), 1, NONE],
    [re.compile(r'^border\-bottom\-left\-radius'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^border\-bottom\-right\-radius'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^border\-image'), 1, FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^border\-image\-outset'), 1, NONE],
    [re.compile(r'^border\-image\-repeat'), 1, NONE],
    [re.compile(r'^border\-image\-slice'), 1, NONE],
    [re.compile(r'^border\-image\-source'), 1, NONE],
    [re.compile(r'^border\-image\-width'), 1, NONE],
    [re.compile(r'^border\-radius'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^border\-top\-left\-radius'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^border\-top\-right\-radius'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^box\-decoration\-break'), 1, NONE],
    [re.compile(r'^box\-align'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^box\-direction'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^box\-flex'), 1, FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^box\-flex\-group'), 1, NONE],
    [re.compile(r'^box\-lines'), 1, NONE],
    [re.compile(r'^box\-ordinal\-group'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^box\-orient'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^box\-pack'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^box\-shadow'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^box\-sizing'), 1, IE8 | IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^color\-profile'), 1, NONE],
    [re.compile(r'^column\-fill'), 1, NONE],
    [re.compile(r'^column\-gap'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-rule'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-rule\-color'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-rule\-style'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-rule\-width'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-span'), 1, IE9PLUS | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-width'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^columns'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^column\-count'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^crop'), 1, NONE],
    [re.compile(r'^dominant\-baseline'), 1, NONE],
    [re.compile(r'^drop\-initial\-after\-adjust'), 1, NONE],
    [re.compile(r'^drop\-initial\-after\-align'), 1, NONE],
    [re.compile(r'^drop\-initial\-before\-adjust'), 1, NONE],
    [re.compile(r'^drop\-initial\-before\-align'), 1, NONE],
    [re.compile(r'^drop\-initial\-size'), 1, NONE],
    [re.compile(r'^drop\-initial\-value'), 1, NONE],
    [re.compile(r'^fit'), 1, NONE],
    [re.compile(r'^fit\-position'), 1, NONE],
    [re.compile(r'^float\-offset'), 1, NONE],
    [re.compile(r'^font\-size\-adjust'), 1, FIREFOX],
    [re.compile(r'^font\-stretch'), 1, NONE],
    [re.compile(r'^grid\-columns'), 1, NONE],
    [re.compile(r'^grid\-rows'), 1, NONE],
    [re.compile(r'^hanging\-punctuation'), 1, NONE],
    [re.compile(r'^hyphenate\-after'), 1, NONE],
    [re.compile(r'^hyphenate\-before'), 1, NONE],
    [re.compile(r'^hyphenate\-characters'), 1, NONE],
    [re.compile(r'^hyphenate\-lines'), 1, NONE],
    [re.compile(r'^hyphenate\-resource'), 1, NONE],
    [re.compile(r'^hyphens'), 1, NONE],
    [re.compile(r'^icon'), 1, NONE],
    [re.compile(r'^image\-orientation'), 1, NONE],
    [re.compile(r'^image\-resolution'), 1, NONE],
    [re.compile(r'^inline\-box\-align'), 1, NONE],
    [re.compile(r'^line\-stacking'), 1, NONE],
    [re.compile(r'^line\-stacking\-ruby'), 1, NONE],
    [re.compile(r'^line\-stacking\-shift'), 1, NONE],
    [re.compile(r'^line\-stacking\-strategy'), 1, NONE],
    [re.compile(r'^mark'), 1, NONE],
    [re.compile(r'^mark\-after'), 1, NONE],
    [re.compile(r'^mark\-before'), 1, NONE],
    [re.compile(r'^marks'), 1, NONE],
    [re.compile(r'^marquee\-direction'), 1, CHROME | SAFARI],
    [re.compile(r'^marquee\-play\-count'), 1, CHROME | SAFARI],
    [re.compile(r'^marquee\-speed'), 1, CHROME | SAFARI],
    [re.compile(r'^marquee\-style'), 1, CHROME | SAFARI],
    [re.compile(r'^move\-to'), 1, NONE],
    [re.compile(r'^nav\-down'), 1, OPERA],
    [re.compile(r'^nav\-index'), 1, OPERA],
    [re.compile(r'^nav\-left'), 1, OPERA],
    [re.compile(r'^nav\-right'), 1, OPERA],
    [re.compile(r'^nav\-up'), 1, OPERA],
    [re.compile(r'^opacity'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^outline\-offset'), 1, FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^overflow\-style'), 1, NONE],
    [re.compile(r'^overflow\-x'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^overflow\-y'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^page'), 1, NONE],
    [re.compile(r'^page\-policy'), 1, NONE],
    [re.compile(r'^perspective'), 1, CHROME | SAFARI],
    [re.compile(r'^perspective\-origin'), 1, CHROME | SAFARI],
    [re.compile(r'^punctuation\-trim'), 1, NONE],
    [re.compile(r'^rendering\-intent'), 1, NONE],
    [re.compile(r'^resize'), 1, FIREFOX | CHROME | SAFARI],
    [re.compile(r'^rest'), 1, NONE],
    [re.compile(r'^rest\-after'), 1, NONE],
    [re.compile(r'^rest\-before'), 1, NONE],
    [re.compile(r'^rotation'), 1, NONE],
    [re.compile(r'^rotation\-point'), 1, NONE],
    [re.compile(r'^ruby\-align'), 1, IE9PLUS],
    [re.compile(r'^ruby\-overhang'), 1, IE9PLUS],
    [re.compile(r'^ruby\-position'), 1, IE9PLUS],
    [re.compile(r'^ruby\-span'), 1, NONE],
    [re.compile(r'^size'), 1, NONE],
    [re.compile(r'^string\-set'), 1, NONE],
    [re.compile(r'^target'), 1, NONE],
    [re.compile(r'^target\-name'), 1, NONE],
    [re.compile(r'^target\-new'), 1, NONE],
    [re.compile(r'^target\-position'), 1, NONE],
    [re.compile(r'^text\-align\-last'), 1, NONE],
    [re.compile(r'^text\-emphasis'), 1, NONE],
    [re.compile(r'^text\-height'), 1, NONE],
    [re.compile(r'^text\-justify'), 1, ALLIE],
    [re.compile(r'^text\-outline'), 1, NONE],
    [re.compile(r'^text\-overflow'), 1, ALLIE | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^text\-shadow'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^text\-wrap'), 1, NONE],
    [re.compile(r'^transform'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^transform\-origin'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^transform\-style'), 1, CHROME | SAFARI],
    [re.compile(r'^transition'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^transition\-property'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^transition\-duration'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^transition\-timing\-function'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^transition\-delay'), 1, IE9PLUS | FIREFOX | CHROME | SAFARI | OPERA],
    [re.compile(r'^word\-break'), 1, ALLIE | FIREFOX | CHROME | SAFARI],
    [re.compile(r'^word\-wrap'), 1, ALLIE | FIREFOX | CHROME | SAFARI | OPERA]
]

# some hacks
RULESET_HACKS = [
    [re.compile(r'\*html'),                 1, IE6],
    [re.compile(r'\*\+html'),               1, IE7],
    [re.compile(r'\*:first\-child\+html'),  1, IE7],
    [re.compile(r'html>body'),              1, IE7 | IE8 | IE9PLUS],
    [re.compile(r'html>/\*\*/body'),        1, IE8 | IE9PLUS],
    [re.compile(r'.*\-webkit\-'),           1, WEBKIT],
    [re.compile(r'.*\-moz\-'),              1, FIREFOX],
    [re.compile(r'.*\-ms\-'),               1, IE9PLUS],
    [re.compile(r'.*\-o\-'),                1, OPERA],

    #auto generated by script AUTO-GENERATOR-2 .
    [re.compile(r'.+:first\-line'), 1, NOIE6],
    [re.compile(r'.+:first\-letter'), 1, NOIE6],
    [re.compile(r'\.[^\s]+\.[^\s]+'), 2, NOIE6],
    [re.compile(r'.+>.+'), 1, NOIE6],
    [re.compile(r'.+:first\-child'), 1, NOIE6],
    [re.compile(r'.+:focus'), 1, NOIE67],
    [re.compile(r'.+\+.+'), 1, NOIE6],
    [re.compile(r'.+\[.+\]'), 1, NOIE6],
    [re.compile(r'.+\[.+=.+\]'), 1, NOIE6],
    [re.compile(r'.+\[.+~=.+\]'), 1, NOIE6],
    [re.compile(r'.+:before'), 1, NOIE67],
    [re.compile(r'.+:after'), 1, NOIE67],
    [re.compile(r'.+~.+'), 1, NOIE6],
    [re.compile(r'.+\[.+\^=.+\]'), 1, NOIE6],
    [re.compile(r'.+\[.+\$=.+\]'), 1, NOIE6],
    [re.compile(r'.+\[.+\*=.+\]'), 1, NOIE6],
    [re.compile(r'.+\[.+\|=.+\]'), 1, NOIE6],
    [re.compile(r'.+:root'), 1, NOIE678],
    [re.compile(r'.+:nth\-of\-type'), 1, NOIE678],
    [re.compile(r'.+:nth\-last\-of\-type'), 1, NOIE678],
    [re.compile(r'.+:first\-of\-type'), 1, NOIE678],
    [re.compile(r'.+:last\-of\-type'), 1, NOIE678],
    [re.compile(r'.+:only\-of\-type'), 1, NOIE678],
    [re.compile(r'.+:only\-child'), 1, NOIE678],
    [re.compile(r'.+:last\-child'), 1, NOIE678],
    [re.compile(r'.+:nth\-child'), 1, NOIE678],
    [re.compile(r'.+:nth\-last\-child'), 1, NOIE678],
    [re.compile(r'.+:empty'), 1, NOIE678],
    [re.compile(r'.+:target'), 1, NOIE678],
    [re.compile(r'.+:checked'), 1, NOIE678],
    [re.compile(r'.+::selection'), 1, NOIE678],
    [re.compile(r'.+:enabled'), 1, NOIE678],
    [re.compile(r'.+:disabled'), 1, NOIE678],
    [re.compile(r'.+:not\(.+\)'), 1, NOIE678]
]

# .test[fd*=df], .test:not(xxx) {
#      width:100px;
# }
# use .test:not(xxx) as important hack
RULESET_HACKS.sort(lambda a, b: a[2] - b[2])

# some hacks
EXTRA_HACKS = [
    [re.compile(r'@\-webkit\-keyframes'),   WEBKIT],
    [re.compile(r'@\-moz\-keyframes'),      FIREFOX],
    [re.compile(r'@\-ms\-keyframes'),       IE9PLUS],
    [re.compile(r'@\-o\-keyframes'),        OPERA],
    [re.compile(r'@keyframes'),             NONEIE | IE9PLUS],
    [re.compile(r'@font\-face'),           IE9PLUS | NONEIE],
    [re.compile(r'@\-moz\-document'),       FIREFOX],
    [re.compile(r'@mediascreenand\(\-webkit\-min\-device\-pixel\-ratio:0\)'),  WEBKIT],
    [re.compile(r'@mediascreenand\(max\-device\-width:480px\)'),               WEBKIT],
    [re.compile(r'@mediaalland\(\-webkit\-min\-device\-pixel\-ratio:10000\),notalland\(\-webkit\-min\-device\-pixel\-ratio:0\)'),  OPERA]
]

def doRuleDetect(name, value):
    name = name.strip().replace(' ', '')
    value = value.strip().replace(' ', '')

    for hack in RULE_HACKS:
        pattern = hack[0]
        match = pattern.match(name if hack[1] == 1 else value)
        if match:
            #print name, value, bin(hack[2])
            return hack[2]
    return STD

def doRuleSetDetect(selector):
    originSelector = selector.strip();
    selector = originSelector.replace(' ', '')
    for hack in RULESET_HACKS:
        pattern = hack[0]
        match = pattern.match(selector if hack[1] == 1 else originSelector)
        if match:
            return hack[2]
    return STD

def doExtraDetect(selector):
    selector = selector.strip().replace(' ', '')
    for hack in EXTRA_HACKS:
        pattern = hack[0]
        match = pattern.match(selector)
        if match:
            return hack[1]
    return STD

if __name__ == '__main__':
    print(bin(doRuleSetDetect('.test [a=1] .test2')))
    #print(bin(doExtraDetect('@media screen and (-webkit-min-device-pixel-ratio:0)')))
    #print(bin(doExtraDetect('@media all and (-webkit-min-device-pixel-ratio:10000), not all and (-webkit-min-device-pixel-ratio:0)')))

#SCRIPT AUTO-GENERATOR-1
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
#    contents.push('[re.compile(r\'^' + prop.replace(/\-/g, '\\-') + '\'), 1, ' + result + '],');
#}
#console.log(contents.join('\n'));

#SCRIPT AUTO-GENERATOR-2
#execute on http://kimblim.dk/css-tests/selectors/
#
#var table = document.querySelectorAll('.testOverview tr')
#collector = []
#for (var i =0, l = table.length; i < l; i++) {
#    tr = table[i];
#    th =  tr.getElementsByTagName('th')[0]    
#    selector = th.firstChild.innerHTML
#    if (!selector) continue
#    selector = selector.replace('E', 'div')
#    selector = selector.replace('F', 'span')
#    selector = selector.replace('&gt;', '>')
#    originSelector = selector
#    
#    //console.log(selector)
#    tds = tr.getElementsByTagName('td');
#    if (tds[2].firstChild.innerHTML == 'No') {
#        res = 'NOIE678'
#    } else if (tds[1].firstChild.innerHTML == 'No') {
#        res = 'NOIE67'
#    } else if (tds[0].firstChild.innerHTML == 'No') {
#        res = 'NOIE6'
#    } else {
#        continue
#    }
#    selector = selector.replace(/\-/g, '\\-')
#    selector = selector.replace(/\*/g, '\\*')
#    selector = selector.replace(/\|/g, '\\|')
#    selector = selector.replace(/\$/g, '\\$')
#    selector = selector.replace(/\^/g, '\\^')
#    selector = selector.replace(/\s/g, '')
#    selector = selector.replace(/\+/g, '\\+')
#    selector = selector.replace(/\[/g, '\\[')
#    selector = selector.replace(/\]/g, '\\]')
#    selector = selector.replace(/\./g, '\\.')
#    selector = selector.replace(/\(s\)/g, '\\(.+\\)')
#    selector = selector.replace('"name"', '.+')
#    selector = selector.replace(/classname/g, '.+')
#    selector = selector.replace(/div|span|attr/g, '.+')
#    //console.log(selector, res)
#    collector.push('    [re.compile(r\'' + selector+ '\', ' + (originSelector == '.classname.classname' ? 2: 1) + '), ' + res + '],')
#}
#console.log(collector.join('\n'))
