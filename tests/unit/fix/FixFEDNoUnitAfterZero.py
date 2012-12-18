from helper import *

def doTest():
    _rgba()
    _rgba_no_space()

def _rgba_no_space():
    css = '''.test1 {
        box-shadow: inset 0 0px 0 0 rgba(0,0px,0px,0.1);
    }'''

    fixer, msg = doFix(css, '')
    expectedFixed = '''.test1 {
    box-shadow: inset 0 0 0 0 rgba(0, 0, 0, .1);
}'''
    equal(msg, expectedFixed, 'rgba no space is also ok')


def _rgba():
    css = '''html {
        -webkit-tap-highlight-color: rgba(0px, 0px, 0px, 0.1);
    }'''

    fixer, msg = doFix(css, '')

    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    color = ruleSet.getRuleByName('tap-highlight-color')
    equal(color.fixedValue, 'rgba(0, 0, 0, .1)', 'tap-highlight-color is fixed')
    equal(color.value, 'rgba(0px, 0px, 0px, 0.1)', 'tap-highlight-color is ok')

    css = '''.current-hot-films-ul {
        -webkit-transition:all 0.5s ease-in-out 0s;
           -moz-transition:all 0.5s ease-in-out 0s; 
             -o-transition:all 0.5s ease-in-out 0s;
                transition:all 0.5s ease-in-out 0s;
    }'''
    expectedFixed = '''.current-hot-films-ul {
    -webkit-transition: all .5s ease-in-out 0s;
       -moz-transition: all .5s ease-in-out 0s;
         -o-transition: all .5s ease-in-out 0s;
            transition: all .5s ease-in-out 0s;
}'''

    fixer, msg = doFix(css, '')
    equal(msg.strip(), expectedFixed.strip(), 'transition is ok, 0s can not be shorter')
