from helper import *

def doTest():
    _handle_complicated_statement()

def _handle_complicated_statement():
    css = '''.ui-bar-a {
    border: 1px solid       #333 /*{a-bar-border}*/;
    background:             #111 /*{a-bar-background-color}*/;
    color:                  #fff /*{a-bar-color}*/;
    font-weight: bold;
    text-shadow: 0 /*{a-bar-shadow-x}*/ -1px /*{a-bar-shadow-y}*/ 1px /*{a-bar-shadow-radius}*/ #000 /*{a-bar-shadow-color}*/;
    background-image: -webkit-gradient(linear, left top, left bottom, from( #3c3c3c /*{a-bar-background-start}*/), to( #111 /*{a-bar-background-end}*/)); /* Saf4+, Chrome */
    background-image: -webkit-linear-gradient( #3c3c3c /*{a-bar-background-start}*/, #111 /*{a-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
    background-image:    -moz-linear-gradient( #3c3c3c /*{a-bar-background-start}*/, #111 /*{a-bar-background-end}*/); /* FF3.6 */
    background-image:     -ms-linear-gradient( #3c3c3c /*{a-bar-background-start}*/, #111 /*{a-bar-background-end}*/); /* IE10 */
    background-image:      -o-linear-gradient( #3c3c3c /*{a-bar-background-start}*/, #111 /*{a-bar-background-end}*/); /* Opera 11.10+ */
    background-image:         linear-gradient( #3c3c3c /*{a-bar-background-start}*/, #111 /*{a-bar-background-end}*/);
}

.ui-bar-a .ui-link-inherit {
    color: #fff /*{a-bar-color}*/;
}'''

    expectedFixed = '''.ui-bar-a {
    border: 1px solid #333;
    background: #111;
    background-image: -webkit-gradient(linear,left top,left bottom,from(#3C3C3C),to(#111));
    background-image: -webkit-linear-gradient(#3C3C3C,#111);
    background-image: -moz-linear-gradient(#3C3C3C,#111);
    background-image: -ms-linear-gradient(#3C3C3C,#111);
    background-image: -o-linear-gradient(#3C3C3C,#111);
    background-image: linear-gradient(#3C3C3C,#111);
    color: #FFF;
    font-weight: bold;
    text-shadow: 0 -1px 1px #000;
}

.ui-bar-a .ui-link-inherit {
    color: #FFF;
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'complicated statement is ok')