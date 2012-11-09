CSSCheckStyle
=============
## Description
<pre>
@description {
	destination: 检查CSS代码中的编码规范和编码风格问题;
	reference: 《人人FED CSS编码规范》;
	language: python;
}
</pre>

## Installation
**easy_install https://github.com/wangjeaf/CSSCheckStyle/archive/master.tar.gz**

## Usage
<pre>
ckstyle                        用默认配置检查当前目录下的所有css文件
ckstyle -h / ckstyle --help    显示帮助
ckstyle file.css               检查单个css
ckstyle dir                    检查目录下的所有css
ckstyle -r dir                 递归检查目录下的所有css
ckstyle -p file.css            检查结果打印到控制台，默认是写file.css.ckstyle.txt文件
ckstyle -r -p dir              同上
ckstyle -c xxx.ini             使用xxx.ini中的配置进行检查
ckstyle -c xxx.ini -r -p       使用xxx.ini中的配置进行递归检查，并将结果输出到控制台
ckstyle -r --extension=.test.txt --include=all --exclude=none --errorLevel=2   使用配置的信息进行检查
</pre>

### Complete Example
<pre>
ckstyle -c xxx.ini -r -p --extension=.test.txt --include=all --exclude=none --errorLevel=2 dirpath
</pre>

## CommandLine Options
<pre>
-h / --help     显示帮助
-r              递归检查所有文件
-p              将结果打印到控制台（同时删除已有的对应的结果文件）
-c / --config   指定配置文件（默认使用~/ckstyle.ini）
--include       指定包含的规则
--exclude       指定除外的规则
--extension     指定扩展名
--errorLevel    指定检查出的异常等级(0-error, 1-warning, 2-log)
</pre>

## Config File Options
<pre>
error-level        [=0] 异常等级
include            [=all] 包含的规则
exclude            [=none] 除外的规则
recursive          [=false] 是否递归检查目录下所有文件
print-flag         [=false] 是否打印到控制台
extension          [=.ckstyle.txt] 指定检查结果文件的扩展名
tab-spaces         [=4] tag宽度
standard           [=standard.css] 给一个标准的css文件，检查时遵照此文件来检查
ignore-rule-sets   [=@unit-test-expecteds] 忽略的一些规则集
</pre>

### Config File Demo
```ini
[config]
error-level = 0
include = all
exclude = none
recursive = false
print-flag = false
extension = .ckstyle.txt
tab-spaces = 4
standard = standard.css
ignore-rule-sets = @unit-test-expecteds
```
## Config Priority
指定的配置项的优先级：
**命令行参数 > 指定的配置文件中的配置 > 默认配置文件路径的配置 > 工具的默认参数**

## Plugin Development
<pre>
放置在ckstyle/plugins目录下的所有文件（Base.py和helper.py除外）
每一个文件都对应一种检查规则，开发时可自行添加和修改。
但是必须满足以下条件：
1、文件中必须包含与文件名相同的类名，比如FEDNoExpression.py中包含FEDNoExpression类
2、类必须继承自RuleChecker/RuleSetChecker/StyleSheetChecker
3、类中必须包含check方法，并且传入rule/ruleSet/styleSheet作为参数，并且返回True(通过)/False(不通过)
4、类中必须包含errorLevel和errorMsg属性，便于检测异常时给出错误提示
5、errorMsg中可以包含 ${selector}/${name}/${value}等属性设置，在错误提示时将进行相应替换
6、每一个规则，需要在tests目录中添加对应的单元测试用例，测试用例请参见"Unit Test"小节
</pre>

### plugin Demo

``` python
from Base import *

class FEDSemicolonAfterValue(RuleChecker):
    def __init__(self):
        self.id = 'add-semicolon'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'each rule in "${selector}" need semicolon in the end, "${name}" has not'
    def check(self, rule):
        if not rule.roughValue.strip().endswith(';'):
            return False
        return True 
```

## Unit Test
<pre>
每一个规则，都需要添加对应的单元测试用例
放置在tests/unit目录下的所有文件，都是单元测试用例文件（asserts.py和helper.py除外）
tests/runUnitTests.py是单元测试运行器，将运行tests/unit的所有单元测试并给出运行结果
</pre>

### Python Unit Test
<pre>
1、必须在文件中引入asserts.py，用于断言
2、必须在文件中加入doTest方法，并在doTest方法及其调用中编写断言
</pre>

### python Unit Test Demo
``` python
from asserts import *
from helper import doCssCheck

def doTest():
    text = 'body {width: 1px}'
    logs, warns, errors = doCssCheck(text)
    equal(len(logs), 2, 'two logs')
    equal(len(warns), 1, 'one warn happened')
    equal(len(errors), 1, 'one error happened')
    equal(warns[0], r'each rule in "body" need semicolon in the end, "width" has not', 'warn rule text is ok')
    equal(errors[0], r'should not set style for html tag in "body"', 'error rule text is ok')
```

### Css Unit Test
<pre>
1、必须包含 @unit-test-expecteds，并在此规则中写入单元测试断言
2、每一个规则由key-value组成，key为错误的errorLevel，value为错误消息
3、如果断言中有，而实际检查结果中没有，测试时将出现[expect but not have]
4、如果断言中没有，而实际检查结果中有，测试时将出现[unexpect but has]
5、一定要注意errorLevel是否正确
</pre>


### CSS Unit Test Demo

``` css
@unit-test-expecteds {
    1: zero should be removed when meet 0.xxx in ".test"
    1: zero should be removed when meet 0.xxx in ".test-another"
    1: zero should be removed when meet 0.xxx in ".test-padding"
}

.test {
    width: 0.1px;
}

.test-another {
    width: 0.001px;
}

.test-padding {
    padding: 1px 0.2px;
}
```

## Rules
<pre>
@all-rules {
    hexadecimal-color:              16进制颜色，大写，并且尽量省略;
    no-font-family:                 不允许业务代码设置字体;
    combine-into-one:               将可以合并的样式设置合并;
    comment-length:                 注释长度不允许超过80个字符;
    css3-with-prefix:               css3前缀相关检查;
    css3-prop-spaces:               css3缩进相关检查;
    no-style-for-simple-selector:   不要为简单选择器设置样式，避免全局覆盖;
    no-style-for-tag:               不要为html tag设置样式;
    font-unit:                      字体的单位必须使用px或pt;
    hack-prop:                      hack属性时的检查;
    hack-ruleset:                   hack规则时的检查;
    high-perf-selector:             针对低性能的选择器的检查;
    multi-line-brace:               代码多行时的括号检查;
    multi-line-selector:            代码多行时的选择器检查;
    multi-line-space:               代码多行时的空格检查;
    add-author:                     需要在文件中添加作者信息;
    no-alpha-image-loader:          不要使用alphaImageLoader;
    no-appearance-word-in-selector: 不要在选择器中出现表现相关的词汇;
    no-comment-in-value:            不要在css属性中添加注释;
    no-empty-ruleset:               删除空的规则;
    no-expression:                  不要使用非一次性表达式;
    number-in-selector:             不要在选择器中使用简单数字1、2、3;
    no-star-in-selector:            不要在选择器中使用星号;
    del-unit-after-zero:            删除0后面的单位;
    no-zero-before-dot:             删除0.2前面的0;
    no-border-zero:                 用border:none替换border:0;
    no-underline-in-selector:       不要在选择器中使用下划线;
    add-semicolon:                  为每一个属性后添加分号;
    do-not-use-important:           不要使用important;
    single-line-brace:              单行的括号检查;
    single-line-selector:           单行的选择器检查;
    single-line-space:              单行的空格检查;
    keep-in-order:                  属性应该按照推荐的顺序编写;
    no-chn-font-family:             不要出现中文的字体设置，改用对应的英文;
    unknown-css-prop:               错误的css属性;
    unknown-html-tag:               错误的html tag;
    lowercase-prop:                 属性应该用小写;
    lowercase-selector:             选择器用小写字母;
    single-quotation:               使用单引号;
    z-index-in-range:               z-index取值应该符合范围要求;
}
</pre>

所有的规则都对应唯一id，并且有独立的检查类，所有的规则类都在`ckstyle/plugins`目录下。
id与类的对应关系如下：

<pre>
@plugin-id-rule-mapping {
    no-font-family: FEDCanNotSetFontFamily;
    no-expression: FEDNoExpression;
    font-unit: FEDFontSizeShouldBePtOrPx;
    single-line-selector: FEDSingleLineSelector;
    multi-line-selector: FEDMultiLineSelectors;
    no-border-zero: FEDReplaceBorderZeroWithBorderNone;
    css3-with-prefix: FEDCss3PropPrefix;
    keep-in-order: FEDStyleShouldInOrder;
    single-line-space: FEDSingleLineSpaces;
    single-line-brace: FEDSingleLineBraces;
    no-underline-in-selector: FEDSelectorNoUnderLine;
    no-style-for-tag: FEDDoNotSetStyleForTagOnly;
    single-quotation: FEDUseSingleQuotation;
    no-comment-in-value: FEDNoCommentInValues;
    high-perf-selector: FEDHighPerformanceSelector;
    css3-prop-spaces: FEDCss3PropSpaces;
    unknown-css-prop: FEDUnknownCssNameChecker;
    multi-line-space: FEDMultiLineSpaces;
    multi-line-brace: FEDMultiLineBraces;
    combine-into-one: FEDCombineInToOne;
    no-appearance-word-in-selector: FEDNoAppearanceNameInSelector;
    no-alpha-image-loader: FEDNoAlphaImageLoader;
    no-zero-before-dot: FEDNoZeroBeforeDot;
    z-index-in-range: FEDZIndexShouldInRange;
    del-unit-after-zero: FEDNoUnitAfterZero;
    no-star-in-selector: FEDNoStarInSelector;
    add-semicolon: FEDSemicolonAfterValue;
    comment-length: FEDCommentLengthLessThan80;
    no-empty-ruleset: FEDNoEmptyRuleSet;
    add-author: FEDMustContainAuthorInfo;
    no-chn-font-family: FEDTransChnFontFamilyNameIntoEng;
    lowercase-selector: FEDUseLowerCaseSelector;
    no-style-for-simple-selector: FEDDoNotSetStyleForSimpleSelector;
    number-in-selector: FEDNoSimpleNumberInSelector;
    do-not-use-important: FEDShouldNotUseImportant;
    lowercase-prop: FEDUseLowerCase;
    hexadecimal-color: FED16ColorShouldUpper;
    hack-ruleset: FEDHackRuleSetInCorrectWay;
    hack-prop: FEDHackAttributeInCorrectWay;
    unknown-html-tag: FEDUnknownHTMLTagName;
}
</pre>

## Join Us
Email: wangjeaf@gmail.com

Websites: <http://fed.renren.com/> | <http://www.renren.com/>
