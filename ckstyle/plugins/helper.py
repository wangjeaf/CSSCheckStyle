def getAttrOrder(attr, strippedName):
    if cssAttrOrders.has_key(attr):
        return cssAttrOrders[attr] + addCss3PrefixValue(strippedName)
    if attr.find('-') != -1:
        splited = attr.split('-')
        while len(splited) != 0:
            splited = splited[0:-1]
            attr = '-'.join(splited)
            if cssAttrOrders.has_key(attr):
                return cssAttrOrders[attr] + addCss3PrefixValue(strippedName)
    return 2000

def addCss3PrefixValue(attr):
    value = 0
    if attr.startswith('-webkit'):
        value = value - 5
    elif attr.startswith('-khtml'):
        value = value - 5
    elif attr.startswith('-moz'):
        value = value - 3
    elif attr.startswith('-ms'):
        value = value - 2
    elif attr.startswith('-o'):
        value = value - 1
    return value

def isHTMLTag(tag):
    return containsInArray(validHTMLTags, tag)

def isCssProp(prop):
    return containsInArray(validCSSAttrs, prop)

def isCss3Prop(prop):
    return containsInArray(allCss3Props, prop)

def canBeCombined(prop):
    prop = prop.strip()
    for x in canBeCombinedProps:
        if prop.startswith(x):
            return x
    return None

def containsChnChar(string):
    try: 
        trans = unicode(string, 'gb2312')
        return len(string) != len(trans)
    except UnicodeDecodeError:
        return True

def isCss3PrefixProp(prop):
    return containsInArray(prefixCss3Props, prop)

def isFontFamilyName(prop):
    prop = prop.lower()
    added = "," + prop + ","
    return containsInArray(fontFamilyNames, prop) or containsInArray(fontFamilyNames, added)

def existsAppearanceWords(selector):
    selector = selector.lower()
    for word in appearanceWords:
        if selector.find(word) != -1:
            return word
    return None

def isSimpleSelector(selector):
    for s in simpleSelectors:
        if s == selector:
            return True
    return False

def containsInArray(array, value):
    return value in array

# according to http://fed.renren.com/archives/1212
cssAttrOrdersMap = {
    0 : ['display', 'position', 'left', 'top', 'bottom', 'right', 'float', 'list-style', 'clear'],
    200 : ['width', 'height', 'margin', 'padding', 'border'],
    400 : ['background'],
    600 : ['line-height'],
    800 : ['color', 'font', 'text-decoration', 'text-align', 'text-indent', 'vertical-align', 'white-space', 'content'],
    1000: ['cursor', 'z-index', 'zoom'],
    1200: ['transform', 'transition', 'animation', 'box-shadow', 'border-radius']
    # 1400 : ['other']
}

# convert 0:a, b to a:0, b:0
cssAttrOrders = {}
for key, value in cssAttrOrdersMap.items():
    counter = 0
    for x in value:
        cssAttrOrders[x] = key + counter
        counter = counter + 10


canBeCombinedProps = 'border margin padding background font'.split(' ')

# execute in http://www.w3schools.com/cssref/css_websafe_fonts.asp
#
# var tables = document.getElementsByClassName('reference');
# var values = [];
# for (var i = 0;  i < tables.length; i++) {
#     trs = tables[i].getElementsByTagName('tr')
#     for(var j = 0; j < trs.length; j++) {
#         td = trs[j].getElementsByTagName('td')[0];
#         if (td) {
#             var text = td.textContent.toLowerCase().trim()
#             var spliteds = text.split(',');
#             for (var k = 0; k < spliteds.length; k++) {
#                 values.push(spliteds[k].trim().replace('"', "'").replace('"', "'"))
#             }
#         }
#     }
# }
# values = values.slice(2);
# console.log(values.sort().join(','));

fontFamilyNames = ("'arial black','book antiqua','comic sans ms','courier new','lucida console','lucida grande','lucida sans unicode','palatino linotype','times new roman','trebuchet ms',arial,charcoal,courier,cursive,gadget,geneva,geneva,helvetica,helvetica,impact,monaco,monospace,monospace,palatino,sans-serif,sans-serif,sans-serif,sans-serif,sans-serif,sans-serif,sans-serif,sans-serif,serif,serif,tahoma,times,verdana" + ",georgia").split(',')

# add slowly and progressively
simpleSelectors = '.nav .sub #main #main2 #sidebar #sidebar2 .header .footer .publisher .box .login .site-nav .side'.split(' ')

# execute in http://www.w3schools.com/cssref/css_colornames.asp
#
#var tables = document.getElementsByClassName('reference');
#var values = [];
#for (var i = 0;  i < tables.length; i++) {
#    trs = tables[i].getElementsByTagName('tr')
#    for(var j = 0; j < trs.length; j++) {
#        td = trs[j].getElementsByTagName('td')[0];
#        if (td) {
#            var text = td.textContent.toLowerCase().trim()
#            if (text == 'h1') text = 'h1 h2 h3 h4 h5 h6';
#            values.push(text)
#        }
#    }
#}
#values = values.slice(2);
#console.log(values.join(' '));

appearanceWords = ("left right top bottom float" + " aqua aquamarine azure beige bisque black blanchedalmond blue blueviolet brown burlywood cadetblue chartreuse chocolate coral cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod darkgray darkgrey darkgreen darkkhaki darkmagenta darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen darkslateblue darkslategray darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue firebrick floralwhite forestgreen fuchsia gainsboro ghostwhite goldenrod gray grey green greenyellow honeydew hotpink indianred indigo ivory khaki lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan lightgoldenrodyellow lightgray lightgrey lightgreen lightpink lightsalmon lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue lightyellow lime limegreen linen magenta maroon mediumaquamarine mediumblue mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen mediumturquoise mediumvioletred midnightblue mintcream mistyrose moccasin navajowhite navy oldlace olive olivedrab orange orangered orchid palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum powderblue purple red rosybrown royalblue saddlebrown salmon sandybrown seagreen seashell sienna silver skyblue slateblue slategray slategrey snow springgreen steelblue thistle tomato turquoise violet wheat white whitesmoke yellow yellowgreen").split(' ')
# execute on http://www.w3schools.com/cssref/default.asp
#
# var tables = document.getElementsByClassName('reference');
# var values = [];
# for (var i = 0;  i < tables.length; i++) {
#     trs = tables[i].getElementsByTagName('tr')
#     for(var j = 0; j < trs.length; j++) {
#         td = trs[j].getElementsByTagName('td')[0];
#         if (td && trs[j].getElementsByTagName('td')[2].textContent == '3') {
#             var text = td.textContent
#             if (text == 'h1') text = 'h1 h2 h3 h4 h5 h6';
#             values.push(text)
#         }
#     }
# }
# values = values.slice(2);
# console.log(values.join(' '));
#
allCss3Props = 'animation-name animation-duration animation-timing-function animation-delay animation-iteration-count animation-direction animation-play-state background-clip background-origin background-size border-bottom-left-radius border-bottom-right-radius border-image border-image-outset border-image-repeat border-image-slice border-image-source border-image-width border-radius border-top-left-radius border-top-right-radius box-decoration-break box-shadow overflow-x overflow-y overflow-style rotation rotation-point color-profile opacity rendering-intent bookmark-label bookmark-level bookmark-target float-offset hyphenate-after hyphenate-before hyphenate-character hyphenate-lines hyphenate-resource hyphens image-resolution marks string-set box-align box-direction box-flex box-flex-group box-lines box-ordinal-group box-orient box-pack @font-face font-size-adjust font-stretch crop move-to page-policy grid-columns grid-rows target target-name target-new target-position alignment-adjust alignment-baseline baseline-shift dominant-baseline drop-initial-after-adjust drop-initial-after-align drop-initial-before-adjust drop-initial-before-align drop-initial-size inline-box-align line-stacking line-stacking-ruby line-stacking-shift line-stacking-strategy text-height marquee-direction marquee-play-count marquee-speed marquee-style column-count column-fill column-gap column-rule column-rule-color column-rule-style column-rule-width column-span column-width columns fit fit-position image-orientation page size ruby-align ruby-overhang ruby-position ruby-span mark mark-after mark-before phonemes rest rest-after rest-before voice-balance voice-duration voice-pitch voice-pitch-range voice-rate voice-stress voice-volume hanging-punctuation punctuation-trim text-align-last text-justify text-outline text-overflow text-shadow text-wrap word-break word-wrap transform transform-origin transform-style perspective perspective-origin backface-visibility transition transition-property transition-duration transition-timing-function transition-delay appearance box-sizing icon nav-down nav-index nav-left nav-right nav-up outline-offset resize'.split(' ')


# from https://github.com/stubbornella/csslint/wiki/Require-compatible-vendor-prefixes
prefixCss3Props = 'animation animation-delay animation-direction animation-duration animation-fill-mode animation-iteration-count animation-name animation-play-state animation-timing-function appearance border-end border-end-color border-end-style border-end-width border-image border-radius border-start border-start-color border-start-style border-start-width box-align box-direction box-flex box-lines box-ordinal-group box-orient box-pack box-sizing box-shadow column-count column-gap column-rule column-rule-color column-rule-style column-rule-width column-width hyphens line-break margin-end margin-start marquee-speed marquee-style padding-end padding-start tab-size text-size-adjust transform transform-origin transition transition-delay transition-duration transition-property transition-timing-function user-modify user-select writing-mode'.split(' ')

# execute on http://www.w3schools.com/tags/default.asp
#
# var tables = document.getElementsByClassName('reference');
# var values = [];
# for (var i = 0;  i < tables.length; i++) {
#     trs = tables[i].getElementsByTagName('tr')
#     for(var j = 0; j < trs.length; j++) {
#         td = trs[j].getElementsByTagName('td')[0];
#         if (td) {
#             var text = td.textContent.split('>')[0].split('<')[1]
#             if (text == 'h1') text = 'h1 h2 h3 h4 h5 h6';
#             values.push(text)
#         }
#     }
# }
# values = values.slice(2);
# console.log(values.join(' '));

validHTMLTags = 'a abbr acronym address applet area article aside audio b base basefont bdi bdo big blockquote body br button canvas caption center cite code col colgroup command datalist dd del details dfn dir div dl dt em embed fieldset figcaption figure font footer form frame frameset h1 h2 h3 h4 h5 h6 head header hgroup hr html i iframe img input ins kbd keygen label legend li link map mark menu meta meter nav noframes noscript object ol optgroup option output p param pre progress q rp rt ruby s samp script section select small source span strike strong style sub summary sup table tbody td textarea tfoot th thead time title tr track tt u ul var video wbr'.split(' ')


# execute on http://www.w3schools.com/cssref/default.asp
#var tables = document.getElementsByClassName('reference');
#var values = [];
#for (var i = 0;  i < tables.length; i++) {
#    trs = tables[i].getElementsByTagName('tr')
#    for(var j = 0; j < trs.length; j++) {
#        td = trs[j].getElementsByTagName('td')[0];
#        if (td) {
#            values.push(td.textContent)
#        }
#    }
#}
#console.log(values.join(' '));

validCSSAttrs = ('@keyframes animation animation-name animation-duration animation-timing-function animation-delay animation-iteration-count animation-direction animation-play-state ' + 
    'background background-attachment background-color background-image background-position background-repeat background-clip background-origin background-size background-inline-policy border border-bottom border-bottom-color border-bottom-style border-bottom-width border-color border-left border-left-color border-left-style border-left-width border-right border-right-color border-right-style border-right-width border-style border-top border-top-color border-top-style border-top-width border-width outline outline-color outline-style outline-width ' + 
    'border-bottom-left-radius border-bottom-right-radius border-image border-image-outset border-image-repeat border-image-slice border-image-source border-image-width border-radius border-top-left-radius border-top-right-radius box-decoration-break box-shadow overflow-x overflow-y overflow-style rotation rotation-point color-profile opacity rendering-intent bookmark-label bookmark-level bookmark-target float-offset ' + 
    'hyphenate-after hyphenate-before hyphenate-character hyphenate-lines hyphenate-resource hyphens image-resolution marks string-set height max-height max-width min-height min-width width box-align box-direction box-flex box-flex-group box-lines box-ordinal-group box-orient box-pack font font-family font-size font-style font-variant font-weight @font-face font-size-adjust font-stretch content counter-increment counter-reset quotes ' + 
    'crop move-to page-policy grid-columns grid-rows target target-name target-new target-position alignment-adjust alignment-baseline baseline-shift dominant-baseline drop-initial-after-adjust drop-initial-after-align drop-initial-before-adjust drop-initial-before-align drop-initial-size drop-initial-value inline-box-align line-stacking line-stacking-ruby line-stacking-shift line-stacking-strategy text-height list-style list-style-image ' + 
    'list-style-position list-style-type margin margin-bottom margin-left margin-right margin-top marquee-direction marquee-play-count marquee-speed marquee-style column-count column-fill column-gap column-rule column-rule-color column-rule-style column-rule-width column-span column-width columns padding padding-bottom padding-left padding-right padding-top fit fit-position image-orientation page size bottom clear clip cursor display ' + 
    'float left overflow position right top visibility z-index orphans page-break-after page-break-before page-break-inside widows ruby-align ruby-overhang ruby-position ruby-span mark mark-after mark-before phonemes rest rest-after rest-before voice-balance voice-duration voice-pitch voice-pitch-range voice-rate ' + 
    'voice-stress voice-volume border-collapse border-spacing caption-side empty-cells table-layout color direction letter-spacing line-height text-align text-decoration text-indent text-transform unicode-bidi vertical-align white-space word-spacing hanging-punctuation punctuation-trim text-align-last text-justify ' + 
    'text-outline text-overflow text-shadow text-wrap word-break word-wrap transform transform-origin transform-style perspective perspective-origin backface-visibility transition transition-property transition-duration transition-timing-function transition-delay appearance box-sizing icon nav-down nav-index nav-left ' + 
    'nav-right nav-up outline-offset resize expression filter zoom behavior').split(' ')

