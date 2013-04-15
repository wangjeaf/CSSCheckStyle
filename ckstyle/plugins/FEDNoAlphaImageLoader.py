#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDNoAlphaImageLoader(RuleChecker):
    
    '''{
        "summary":"不要使用AlphaImageLoader",
        "desc":"<code>AlphaImageLoader</code> 主要用于在IE6下显示半透明图片，此举实际上费力不讨好，
            对IE的性能影响极大，为了更好地实现网页的 <strong>渐进增强</strong> 
            ，建议不要使用 <code>AlphaImageLoader</code>"
    }'''

    def __init__(self):
        self.id = 'no-alpha-image-loader'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'should not use AlphaImageLoader in "${selector}"'

    def check(self, rule, config):
        if rule.value.find('AlphaImageLoader') != -1:
            return False
        return True 
