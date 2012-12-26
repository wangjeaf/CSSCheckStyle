from helper import *

def doTest():
    _handle_nested_statement()

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