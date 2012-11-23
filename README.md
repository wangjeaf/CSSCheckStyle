CSSCheckStyle
=============
## Description
<pre>
@description {
	destination: 检查CSS代码中的编码规范和编码风格问题;
    good-news: 初步对比各大工具（包括YUI compressor和各种在线工具），确定初步达到业内领先水平，后期任重道远;
	reference: <a href="http://fed.renren.com/archives/1212">《人人FED CSS编码规范》</a>;
	language: python;
    what-can-i-do-for-css: check -> fix -> combine-attr -> reorder -> combine -> compress;
}
</pre>

## Installation
**easy_install https://github.com/wangjeaf/CSSCheckStyle/archive/master.tar.gz**

## TODOs
* standard.css支持 tellme
* 自动fix CSS代码 fixer
* 代码压缩工具 compressor
* 自动按照推荐顺序排列 orderer
* 自动合并子样式 combiner
* import导入文件的支持 importer
* 完善检查规则
* 收集全站样式与文件的映射关系，并将此映射关系加入配置 [global-styles]

## fix -> reorder -> combine -> compress DEMO
### 说明
以下是通过自动fix，自动排序，自动合并，自动压缩以后的代码示例。

结果来自plugins/*.py中的fix方法，以及entity/*.py的compress方法。

对于fix，目前只做了以下两个plugin的fix：
* FED16ColorShouldUpper
* FEDUseSingleQuotation

其他的fix只需要在对应的plugin文件中添加fix方法，即可实现fix和压缩

### before
```css
.test1 {
    width: 100px;
    height: 200px;
    *display: none;
    border: 1px solid #FFFFFF;
    _display: inline-block;
}

.test2 {
    *display: none;
    width: 100px;
    border: 1px solid #FFF;
    height: 200px;
    _display: inline-block;
}

.test3 {
    border: 1px solid #fff;
    width: 100px;
    height: 200px;
    *display: none;
    _display: inline-block;
}

.test4 {
    border: 1px solid #ffffff;
    *display: none;
    width: 100px;
    height: 200px;
    _display: inline-block;
}

.test5 {
    width: 100px; *display: none; height: 200px;
    border: 1px solid #ffffff;
    _display: inline-block;
}

```

### after
```css
.test1,.test2,.test3,.test4,.test5{*display:none;_display:inline-block;width:100px;height:200px;border:1px solid #FFF}
```

## check Demo
此处演示的是代码风格检查功能。

所有的检查项都来自于plugins/*.py的check方法

### 原始CSS代码
```css
.test1 ul li a {
width:10px;
color:#ffffff;
    -webkit-border-radius:3px;
-moz-border-radius : 3px;
border-radius:3px
}
```
### 检查与修改过程
#### 检查结果 1：
<pre>
[ERROR] 1. use less tag in ".test1 ul li a"
[ERROR] 2. css3 prop "-webkit-border-radius" missing some of "-webkit-,-moz-,-o-,std" in ".test1 ul li a"
[ERROR] 3. css3 prop "-moz-border-radius" missing some of "-webkit-,-moz-,-o-,std" in ".test1 ul li a"
[ERROR] 4. css3 prop "border-radius" missing some of "-webkit-,-moz-,-o-,std" in ".test1 ul li a"
 [WARN] 5. do not simply use 1,2,3 as selector, in ".test1 ul li a"
 [WARN] 6. color should in upper case in ".test1 ul li a"
 [WARN] 7. css3 prop "-moz-border-radius" should align to right in ".test1 ul li a"
 [WARN] 8. css3 prop "border-radius" should align to right in ".test1 ul li a"
 [WARN] 9. should have 4 spaces before "width" in ".test1 ul li a"
 [WARN] 10. should have 4 spaces before "color" in ".test1 ul li a"
 [WARN] 11. should have (only) one "space" before value of "-webkit-border-radius" in ".test1 ul li a"
 [WARN] 12. should not have "space" after "-moz-border-radius" in ".test1 ul li a"
 [WARN] 13. should have (only) one "space" before value of "border-radius" in ".test1 ul li a"
 [WARN] 14. each rule in ".test1 ul li a" need semicolon in the end, "border-radius" has not
</pre>

#### 第一次修改后：

```css
.test-special-word a.a-class {
    width:10px;
    color:#FFFFFF;
    -webkit-border-radius: 3px;
       -moz-border-radius: 3px;
         -o-border-radius: 3px;
            border-radius: 3px;
}
```

#### 再次检查：
<pre>
[ERROR] 1. should not put "HTMLtag" and ".class" together in ".test-special-word a.a-class"
 [WARN] 2. replace "#FFFFFF" with "#FFF" in ".test-special-word a.a-class"
 [WARN] 3. should have (only) one "space" before value of "width" in ".test-special-word a.a-class"
 [WARN] 4. should have (only) one "space" before value of "color" in ".test-special-word a.a-class"
</pre>

#### 符合规范的最终代码

```css
.test-special-word .a-class {
    width: 10px;
    color: #FFF;
    -webkit-border-radius: 3px;
       -moz-border-radius: 3px;
         -o-border-radius: 3px;
            border-radius: 3px;
}
```

目前自动fix检查错误的工具正在紧锣密鼓开发中。

目前架构已经搭建好，需要做的事情，就是在plugins/*.py中，参照check，写一个对应的fix即可~~~

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

## Config File
可通过以下三个方式来指定配置文件：
* 命令行通过-c 或 --config来指定配置文件路径
* 在执行ckstyle命令的当前目录下添加 ckstyle.ini，则默认获取此配置文件
* 在用户默认目录放入ckstyle.ini

## Config File Options
<pre>
error-level        [=0] 异常等级
include            [=all] 包含的规则
exclude            [=none] 除外的规则
recursive          [=false] 是否递归检查目录下所有文件
print-flag         [=false] 是否打印到控制台
extension          [=.ckstyle.txt] 指定检查结果文件的扩展名
tab-spaces         [=4] 一个tab占4个空格宽度
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
