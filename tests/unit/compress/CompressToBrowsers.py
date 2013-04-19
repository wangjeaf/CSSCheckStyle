from helper import *

def doTest():
    _basic()
    _combine()
    _w3school_css3()
    _kimblim_selectors()

def _basic():
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-webkit-transform:1s;-moz-transform:1s;-o-transform:1s}b{width:300px;-moz-transform:1s}', checker.doCompress(STD | NONEIE), 'std is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-webkit-transform:1s}b{width:300px}', checker.doCompress(STD | WEBKIT), 'webkit is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-o-transform:1s}b{width:300px}', checker.doCompress(STD | OPERA), 'opera is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-webkit-transform:1s}b{width:300px}', checker.doCompress(STD | CHROME), 'chrome is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('a{-moz-transform:1s}b{width:300px;-moz-transform:1s}', checker.doCompress(STD | FIREFOX), 'firefox is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('*html a{width:100px}b{width:300px;_width:400px}', checker.doCompress(STD | IE6), 'ie6 is ok')
    checker = doCssFileCompress2('_browsers.css')
    equal('*+html a{width:200px}b{width:300px}', checker.doCompress(STD | IE7), 'ie7 is ok')

def _combine():
	checker = doCssFileCompress2('_browsers_combine_ruleset.css')
	equal('a,b,d{width:300px;-moz-transform:1s}', checker.doCompress(STD | FIREFOX), 'firefox is ok')
	checker = doCssFileCompress2('_browsers_combine_ruleset.css')
	equal('a{width:300px;-webkit-transform:1s}b,d{width:300px}', checker.doCompress(STD | CHROME), 'chrome 2 is ok')

def _w3school_css3():
    checker = doCssFileCompress2('_browsers_from_w3school.css')
    equal('.test{background-clip:test;background-origin:test;animation:test;animation-delay:test;animation-direction:test;animation-duration:test;animation-iteration-count:test;animation-name:test;animation-play-state:test;animation-timing-function:test;appearance:test;border-image:test;border-image-outset:test;border-image-repeat:test;border-image-slice:test;border-image-source:test;border-image-width:test;border-bottom-left-radius:test;border-bottom-right-radius:test;border-radius:test;border-top-left-radius:test;border-top-right-radius:test;box-align:test;box-direction:test;box-flex:test;box-flex-group:test;box-ordinal-group:test;box-orient:test;box-pack:test;box-sizing:test;box-shadow:test;column-count:test;column-gap:test;column-rule:test;column-rule-color:test;column-rule-style:test;column-rule-width:test;column-width:test;marquee-speed:test;marquee-style:test;transform:test;transform-style:test;transform-origin:test;transition:test;transition-delay:test;transition-duration:test;transition-property:test;transition-timing-function:test;background-size:test;backface-visibility:test;column-span:test;columns:test;marquee-direction:test;marquee-play-count:test;opacity:test;outline-offset:test;overflow-x:test;overflow-y:test;perspective:test;perspective-origin:test;resize:test;text-overflow:test;text-shadow:test;word-break:test;word-wrap:test}', 
        checker.doCompress(STD | CHROME), 'chrome w3c is ok')

    equal('.test{background-clip:test;background-origin:test;font-size-adjust:test;animation:test;animation-delay:test;animation-direction:test;animation-duration:test;animation-iteration-count:test;animation-name:test;animation-play-state:test;animation-timing-function:test;appearance:test;border-image:test;border-image-outset:test;border-image-repeat:test;border-image-slice:test;border-image-source:test;border-image-width:test;border-bottom-left-radius:test;border-bottom-right-radius:test;border-radius:test;border-top-left-radius:test;border-top-right-radius:test;box-align:test;box-direction:test;box-flex:test;box-flex-group:test;box-ordinal-group:test;box-orient:test;box-pack:test;box-sizing:test;box-shadow:test;column-count:test;column-gap:test;column-rule:test;column-rule-color:test;column-rule-style:test;column-rule-width:test;column-width:test;transform:test;transform-style:test;transform-origin:test;transition:test;transition-delay:test;transition-duration:test;transition-property:test;transition-timing-function:test;background-size:test;backface-visibility:test;columns:test;opacity:test;outline-offset:test;overflow-x:test;overflow-y:test;resize:test;text-overflow:test;text-shadow:test;word-break:test;word-wrap:test}', 
        checker.doCompress(STD | FIREFOX), 'firefox w3c is ok')

    equal('.test{background-clip:test;background-origin:test;animation:test;animation-delay:test;animation-direction:test;animation-duration:test;animation-iteration-count:test;animation-name:test;animation-play-state:test;animation-timing-function:test;border-image:test;border-image-outset:test;border-image-repeat:test;border-image-slice:test;border-image-source:test;border-image-width:test;border-bottom-left-radius:test;border-bottom-right-radius:test;border-radius:test;border-top-left-radius:test;border-top-right-radius:test;box-flex:test;box-flex-group:test;box-sizing:test;box-shadow:test;column-count:test;column-gap:test;column-rule:test;column-rule-color:test;column-rule-style:test;column-rule-width:test;column-width:test;transform:test;transform-style:test;transform-origin:test;transition:test;transition-delay:test;transition-duration:test;transition-property:test;transition-timing-function:test;background-size:test;column-span:test;columns:test;nav-down:test;nav-index:test;nav-left:test;nav-right:test;nav-up:test;opacity:test;outline-offset:test;overflow-x:test;overflow-y:test;text-overflow:test;text-shadow:test;word-wrap:test}', 
        checker.doCompress(STD | OPERA), 'opera w3c is ok')

    equal('.test{background-clip:test;background-origin:test;animation:test;animation-delay:test;animation-direction:test;animation-duration:test;animation-iteration-count:test;animation-name:test;animation-play-state:test;animation-timing-function:test;appearance:test;border-image:test;border-image-outset:test;border-image-repeat:test;border-image-slice:test;border-image-source:test;border-image-width:test;border-bottom-left-radius:test;border-bottom-right-radius:test;border-radius:test;border-top-left-radius:test;border-top-right-radius:test;box-align:test;box-direction:test;box-flex:test;box-flex-group:test;box-ordinal-group:test;box-orient:test;box-pack:test;box-sizing:test;box-shadow:test;column-count:test;column-gap:test;column-rule:test;column-rule-color:test;column-rule-style:test;column-rule-width:test;column-width:test;marquee-speed:test;marquee-style:test;transform:test;transform-style:test;transform-origin:test;transition:test;transition-delay:test;transition-duration:test;transition-property:test;transition-timing-function:test;background-size:test;backface-visibility:test;column-span:test;columns:test;marquee-direction:test;marquee-play-count:test;opacity:test;outline-offset:test;overflow-x:test;overflow-y:test;perspective:test;perspective-origin:test;resize:test;text-overflow:test;text-shadow:test;word-break:test;word-wrap:test}', 
        checker.doCompress(STD | SAFARI), 'safari w3c is ok')

    equal('.test{text-justify:test;text-overflow:test;word-break:test;word-wrap:test}', 
        checker.doCompress(STD | IE6), 'ie6 w3c is ok')

    equal('.test{text-justify:test;text-overflow:test;word-break:test;word-wrap:test}', 
        checker.doCompress(STD | IE7), 'ie7 w3c is ok')

    equal('.test{background-clip:test;background-origin:test;animation:test;animation-delay:test;animation-direction:test;animation-duration:test;animation-iteration-count:test;animation-name:test;animation-play-state:test;animation-timing-function:test;border-bottom-left-radius:test;border-bottom-right-radius:test;border-radius:test;border-top-left-radius:test;border-top-right-radius:test;box-sizing:test;box-shadow:test;column-count:test;column-gap:test;column-rule:test;column-rule-color:test;column-rule-style:test;column-rule-width:test;column-width:test;transform:test;transform-style:test;transform-origin:test;transition:test;transition-delay:test;transition-duration:test;transition-property:test;transition-timing-function:test;background-size:test;backface-visibility:test;column-span:test;columns:test;opacity:test;overflow-x:test;overflow-y:test;ruby-align:test;ruby-overhang:test;ruby-position:test;text-justify:test;text-overflow:test;text-shadow:test;word-break:test;word-wrap:test}', 
        checker.doCompress(STD | IE9PLUS), 'ie9+ w3c is ok')

def _kimblim_selectors():
    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}div:first-line,div:first-letter,.classname.classname,div > span,div:first-child,div + span,div[attr],div[attr="name"],div[attr~="name"],div ~ span,div[attr^="name"],div[attr$="name"],div[attr*="name"],div[attr|="name"]{width:100px}div:focus,div:before,div:after{width:100px}div:root,div:nth-of-type,div:nth-last-of-type,div:first-of-type,div:last-of-type,div:only-of-type,div:only-child,div:last-child,div:nth-child,div:nth-last-child,div:empty,div:target,div:checked,div::selection,div:enabled,div:disabled,div:not(s){width:100px}'
    equal(res, checker.doCompress(STD | NONEIE), 'std selectors is ok')

    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}'
    equal(res, checker.doCompress(STD | IE6), 'ie6 selectors is ok')

    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}div:first-line,div:first-letter,.classname.classname,div > span,div:first-child,div + span,div[attr],div[attr="name"],div[attr~="name"],div ~ span,div[attr^="name"],div[attr$="name"],div[attr*="name"],div[attr|="name"]{width:100px}'
    equal(res, checker.doCompress(STD | IE7), 'ie7 selectors is ok')

    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}div:first-line,div:first-letter,.classname.classname,div > span,div:first-child,div + span,div[attr],div[attr="name"],div[attr~="name"],div ~ span,div[attr^="name"],div[attr$="name"],div[attr*="name"],div[attr|="name"]{width:100px}div:focus,div:before,div:after{width:100px}'
    equal(res, checker.doCompress(STD | IE8), 'ie8 selectors is ok')

    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}div:first-line,div:first-letter,.classname.classname,div > span,div:first-child,div + span,div[attr],div[attr="name"],div[attr~="name"],div ~ span,div[attr^="name"],div[attr$="name"],div[attr*="name"],div[attr|="name"]{width:100px}div:focus,div:before,div:after{width:100px}div:root,div:nth-of-type,div:nth-last-of-type,div:first-of-type,div:last-of-type,div:only-of-type,div:only-child,div:last-child,div:nth-child,div:nth-last-child,div:empty,div:target,div:checked,div::selection,div:enabled,div:disabled,div:not(s){width:100px}'
    equal(res, checker.doCompress(STD | IE9PLUS), 'ie9 selectors is ok')

    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}div:first-line,div:first-letter,.classname.classname,div > span,div:first-child,div + span,div[attr],div[attr="name"],div[attr~="name"],div ~ span,div[attr^="name"],div[attr$="name"],div[attr*="name"],div[attr|="name"]{width:100px}div:focus,div:before,div:after{width:100px}div:root,div:nth-of-type,div:nth-last-of-type,div:first-of-type,div:last-of-type,div:only-of-type,div:only-child,div:last-child,div:nth-child,div:nth-last-child,div:empty,div:target,div:checked,div::selection,div:enabled,div:disabled,div:not(s){width:100px}'
    equal(res, checker.doCompress(STD | OPERA), 'OPERA selectors is ok')

    checker = doCssFileCompress2('_selectors_from_kimblim.css')
    res = 'div,div span,:link,div:active,div:visited,div.classname,div#id,*,div:hover{width:100px}div:first-line,div:first-letter,.classname.classname,div > span,div:first-child,div + span,div[attr],div[attr="name"],div[attr~="name"],div ~ span,div[attr^="name"],div[attr$="name"],div[attr*="name"],div[attr|="name"]{width:100px}div:focus,div:before,div:after{width:100px}div:root,div:nth-of-type,div:nth-last-of-type,div:first-of-type,div:last-of-type,div:only-of-type,div:only-child,div:last-child,div:nth-child,div:nth-last-child,div:empty,div:target,div:checked,div::selection,div:enabled,div:disabled,div:not(s){width:100px}'
    equal(res, checker.doCompress(STD | WEBKIT), 'WEBKIT selectors is ok')
