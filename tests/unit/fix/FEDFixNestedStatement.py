from helper import *

def doTest():
    _handle_nested_statement()
    _handle_nested_statement_qipa()

def _handle_nested_statement():
    css = '''@media screen and (-webkit-min-device-pixel-ratio:0) {
 .publisher-c .global-publisher-selector{ top:5px;}
 .publisher-a .global-publisher-selector-status a,
 .publisher-a .global-publisher-selector-status .global-publisher-status-trigger:hover,
 .publisher-a .global-publisher-selector .active .global-publisher-status-trigger {
    background-position: 0 1px;
}
 .publisher-a .global-publisher-selector-share a,
 .publisher-a .global-publisher-selector-share a:hover,
 .publisher-a .global-publisher-selector .active .global-publisher-share-trigger{
    background-position: 0 -48px;
 }
}'''

    expectedFixed = '''@media screen and (-webkit-min-device-pixel-ratio:0) {
    .publisher-c .global-publisher-selector {
        top: 5px;
    }
    
    .publisher-a .global-publisher-selector-status a,
    .publisher-a .global-publisher-selector-status .global-publisher-status-trigger:hover,
    .publisher-a .global-publisher-selector .active .global-publisher-status-trigger {
        background-position: 0 1px;
    }
    
    .publisher-a .global-publisher-selector-share a,
    .publisher-a .global-publisher-selector-share a:hover,
    .publisher-a .global-publisher-selector .active .global-publisher-share-trigger {
        background-position: 0 -48px;
    }
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'nested statement is ok')

def _handle_nested_statement_qipa():
    css = '''@-moz-keyframes hinge {
    0% { -moz-transform: rotate(0); -o-transform: rotate(0); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }    
    20%, 60% { -moz-transform: rotate(80deg); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }   
    40% { -moz-transform: rotate(60deg); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }    
    80% { -moz-transform: rotate(60deg) translateY(0); opacity: 1; -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }  
    100% { -moz-transform: translateY(700px); opacity: 0; }
}'''

    expectedFixed = '''@-moz-keyframes hinge {
    0% {
        -moz-animation-timing-function: ease-in-out;
           -moz-transform: rotate(0);
             -o-transform: rotate(0);
        -moz-transform-origin: top left;
    }
    
    20%,
    60% {
        -moz-animation-timing-function: ease-in-out;
        -moz-transform: rotate(80deg);
        -moz-transform-origin: top left;
    }
    
    40% {
        -moz-animation-timing-function: ease-in-out;
        -moz-transform: rotate(60deg);
        -moz-transform-origin: top left;
    }
    
    80% {
        -moz-animation-timing-function: ease-in-out;
        -moz-transform: rotate(60deg) translateY(0);
        -moz-transform-origin: top left;
        opacity: 1;
    }
    
    100% {
        -moz-transform: translateY(700px);
        opacity: 0;
    }
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'qipa nested statement is ok')

    