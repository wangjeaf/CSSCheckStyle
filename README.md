CSSCheckStyle
=============
## Catalog
* <a href="https://github.com/wangjeaf/CSSCheckStyle#description">Description</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#installation">Installation</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#editor-plugins">Editor plugins</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#demo-parse---fix---compress">Demo (parse -> fix -> compress)</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#demo-parse---check">Demo (parse -> check)</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#usage">Usage</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#config-file">Config File</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#plugin-development">Plugin Development</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#unit-test">Unit Test</a>
* <a href="https://github.com/wangjeaf/CSSCheckStyle#rulesplugins">Rules(Plugins)</a>

## Description
<pre>
@description {
	destination: 检查CSS代码中的编码规范和编码风格问题;
    blog: <a href="http://fed.renren.com/archives/1427">《CSSCheckStyle——CSS的解析、检查、修复和压缩》</a>;
    good-news: 初步对比各大工具（包括YUI compressor和各种在线工具），确定初步达到业内领先水平，后期任重道远;
	reference: <a href="http://fed.renren.com/archives/1212">《人人FED CSS编码规范》</a>;
    what-can-i-do: parse -> check -> fix -> combine-attr -> reorder -> combine -> compress;
    export-tools: ckstyle(检查) / fixstyle(修复) / compress(压缩)
    docs: <a href="https://github.com/wangjeaf/CSSCheckStyle-docs">https://github.com/wangjeaf/CSSCheckStyle-docs</a>
	language: python;
}
</pre>

## Installation
**easy_install https://github.com/wangjeaf/CSSCheckStyle/archive/master.tar.gz**

## Editor plugins
目前已经为 VIM / Sublime Text 2 / Notepad ++ 开发了ckstyle插件，可供使用。

不同编辑器实现的命令调用方式如下：

* VIM（command命令）
* Sublime Text 2（快捷键Ctrl+F1，右键菜单项，tools菜单项）
* notepad++（快捷键Ctrl+F1，宏菜单项）
* EditPlus（工具菜单项，快捷键）

各编辑器插件均实现了以下几种操作：
* Fixstyle（自动修复CSS代码）
* FixstyleSafe（安全模式下自动修复CSS代码，目前仅排除合并规则集）
* FixstyleSingleLine（修复成单行模式）
* CkStyle（检查代码问题）
* CssCompress（压缩CSS代码）

所有编辑器插件都在 `editor-plugins` 目录下。

目前插件的功能还比较初级，热烈欢迎熟悉插件开发的同学来贡献编辑器插件。

## Demo (parse -> fix -> compress)
### 说明
以下是通过自动fix，自动排序，自动合并，自动压缩以后的代码示例。

结果来自plugins/*.py中的fix方法，以及entity/*.py的compress方法。

对于fix，目前只做了以下几个plugin的fix：
* FEDHexColorShouldUpper
* FEDUseSingleQuotation
* FEDCombineInToOne (通过combiner的方式灵活扩展，目前只做了MarginCombiner)

其他的fix只需要在对应的plugin文件中添加fix方法，即可实现fix和压缩

此Demo执行的命令： `compress -p test.css`
### before
```css
.test1 {
    width: 100px;
    height: 200px;
    *display: none;
    border: 1px solid #FFFFFF;
    _display: inline-block;
    margin: 10px;
    margin-top: 20px;
}

.test2 {
    *display: none;
    width: 100px;
    border: 1px solid #FFF;
    height: 200px;
    _display: inline-block;
    margin: 20px 10px 10px;
}

.test3 {
    margin: 0 10px 20px;
    border: 1px solid #fff;
    width: 100px;
    height: 200px;
    *display: none;
    _display: inline-block;
    margin-top: 20px;
    margin-left: 10px;
    margin-right: 10px;
    margin-bottom: 10px;
}

.test4 {
    border: 1px solid #ffffff;
    *display: none;
    width: 100px;
    height: 200px;
    margin: 10px;
    _display: inline-block;
    margin-top: 20px;
}

.test5 {
    margin: 10px;
    margin-top: 20px;
    width: 100px; *display: none; height: 200px;
    border: 1px solid #ffffff;
    _display: inline-block;
    margin-left: 10px;
}
```
### fixstyle
`fixstyle` 自动修复以后的代码：
```css
.test1,
.test2,
.test3,
.test4,
.test5 {
    *display: none;
    _display: inline-block;
    width: 100px;
    height: 200px;
    margin: 20px 10px 10px;
    border: 1px solid #FFF;
}
```

`fixstyle --singleLine` 自动修复后的代码：
```css
.test1,
.test2,
.test3,
.test4,
.test5 { *display: none; _display: inline-block; width: 100px; height: 200px; margin: 20px 10px 10px; border: 1px solid #FFF; }
```

### after compress
本压缩工具的压缩结果（属性排列顺序已经按照推荐顺序优化），压缩率： 140 / 766 = 18.3%：
```css
.test1,.test2,.test3,.test4,.test5{*display:none;_display:inline-block;width:100px;height:200px;margin:20px 10px 10px;border:1px solid #FFF}
```

<a href="http://www.cssoptimiser.com">CSS Optimizer</a> 压缩结果，压缩率：310 / 766 = 40.5%：
```css
.test1,.test2,.test3,.test4,.test5{width:100px;height:200px;*display:none;_display:inline-block}.test1,.test3,.test4,.test5{border:1px solid #fff}.test1,.test4,.test5{margin:10px;margin-top:20px}.test2{border:1px solid #FFF}.test2,.test3{margin:20px 10px 10px}.test3{margin:0 10px 20px}.test5{margin-left:10px}
```

YUI Compressor 压缩结果，压缩率：662 / 766 = 86.4%：
```css
.test1{width:100px;height:200px;*display:none;border:1px solid #fff;_display:inline-block;margin:10px;margin-top:20px}.test2{*display:none;width:100px;border:1px solid #FFF;height:200px;_display:inline-block;margin:20px 10px 10px}.test3{margin:0 10px 20px;border:1px solid #fff;width:100px;height:200px;*display:none;_display:inline-block;margin-top:20px;margin-left:10px;margin-right:10px;margin-bottom:10px}.test4{border:1px solid #fff;*display:none;width:100px;height:200px;margin:10px;_display:inline-block;margin-top:20px}.test5{margin:10px;margin-top:20px;width:100px;*display:none;height:200px;border:1px solid #fff;_display:inline-block;margin-left:10px}
```

## Demo (parse -> check)
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
 [WARN] 7. each rule in ".test1 ul li a" need semicolon in the end, "border-radius" has not
  [LOG] 8. css3 prop "-moz-border-radius" should align to right in ".test1 ul li a"
  [LOG] 9. css3 prop "border-radius" should align to right in ".test1 ul li a"
  [LOG] 10. should have 4 spaces before "width" in ".test1 ul li a"
  [LOG] 11. should have 4 spaces before "color" in ".test1 ul li a"
  [LOG] 12. should have (only) one "space" before value of "-webkit-border-radius" in ".test1 ul li a"
  [LOG] 13. should not have "space" after "-moz-border-radius" in ".test1 ul li a"
  [LOG] 14. should have (only) one "space" before value of "border-radius" in ".test1 ul li a"
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
  [LOG] 3. should have (only) one "space" before value of "width" in ".test-special-word a.a-class"
  [LOG] 4. should have (only) one "space" before value of "color" in ".test-special-word a.a-class"
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
## Usage
### 关于ckstyle / fixstyle / compress(csscompress)的命令行参数说明
通过 command -h / command --help可以查看命令的帮助，例如： `compress -h`  `compress --help`

ckstyle(检查)/fixstyle(自动修复)/compress(压缩，同名工具csscompress) 三个工具的命令行参数基本相同

不同之处：
* fixstyle给出了额外的参数：--fixedExtension（修复后文件的扩展名）, --singleLine（自动修复并以单行模式格式化），--safeMode（安全模式，不做某些“本工具不能完全保证正确”的修复）
* compress给出了额外的参数：--safeMode（安全模式，不做某些“本工具不能完全保证正确”的修复），--browsers（是否分浏览器压缩）, --compressExtension（压缩后文件的扩展名）, --combineFile（是否将多个压缩后文件合并），这些参数目前有的尚未实现~~~

### Examples
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

ckstyle -c xxx.ini -r -p --extension=.test.txt --include=all --exclude=none --errorLevel=2 dirpath
</pre>

### CommandLine Options
<pre>
-h / --help     显示帮助
-r              递归检查所有文件
-p              将结果打印到控制台（同时删除已有的对应的结果文件）
-c / --config   指定配置文件（默认使用~/ckstyle.ini）
--include       指定包含的规则（多个规则请以逗号分隔，例如: rule1,rule2,rule3）
--exclude       指定除外的规则（格式同--include）
--extension     指定扩展名
--errorLevel    指定检查出的异常等级(0-error, 1-warning, 2-log)

// for fix and compress
--fixedExtension 修复后文件的扩展名，如.fixed.css，none为替换原文件（将生成一个.bak文件保存原文件）
--compressExtension 压缩后文件的扩展名，如.min.css，none为替换原文件（将生成一个.bak文件保存原文件）
--safeMode      修复和压缩的安全模式
--singleLine    自动修复成单行模式（默认是多行模式）
</pre>

### Config File
可通过以下三个方式来指定配置文件：

* 命令行通过-c 或 --config来指定配置文件路径
* 在执行ckstyle命令的当前目录下添加 ckstyle.ini，则默认获取此配置文件
* 在用户默认目录放入ckstyle.ini

#### Config File Options
<pre>
error-level        [=0] 异常等级
include            [=all] 包含的规则
exclude            [=none] 除外的规则
recursive          [=false] 是否递归检查目录下所有文件
print-flag         [=false] 是否打印到控制台
extension          [=.ckstyle.txt] 指定检查结果文件的扩展名
standard           [=standard.css] 给一个标准的css文件，检查时遵照此文件来检查
ignore-rule-sets   [=@unit-test-expecteds] 忽略的一些规则集
fixed-extension    [=.fixed.css] 修复后文件的扩展名
fix-to-single-line [=false] 是否自动修复成一行
safe-mode          [=false] 是否尝试做某些“本工具不能完全保证正确”的修复，true为不尝试，false为尝试

extension(compress)[=.min.css] 压缩后的文件扩展名
combine-file       [=all.min.css] 压缩多个文件合并成一个的文件名
browsers           [=false] 针对不同浏览器生成不同的压缩后文件
</pre>

#### Config File Demo
```ini
[ckstyle]
error-level = 0
include = all
exclude = none
recursive = false
print-flag = false
extension = .ckstyle.txt
standard = standard.css
ignore-rule-sets = @unit-test-expecteds
fixed-extension = .fixed.css
fix-to-single-line = false
safe-mode = false

[compress]
extension = .min.css
combine-file = all.min.css(todo)
browsers = false

[css-format(todo)]
tab-spaces = 4

[global-selectors(todo)]
.nav, sidebar2 = home-frame2.css
```
### Config Priority
配置项的优先级：
**命令行参数 > 指定的配置文件 > 当前路径下的配置文件 > 用户目录下的配置文件 > 工具的默认参数**

## Plugin Development
放置在`ckstyle/plugins`目录下的所有文件（Base.py和helper.py除外），每一个文件都对应一种检查规则。

开发时可自行添加和修改，但是必须满足以下条件：

1、文件中必须包含与文件名相同的类名，比如FEDNoExpression.py中包含FEDNoExpression类

2、类必须继承自RuleChecker/RuleSetChecker/StyleSheetChecker

3、类中必须包含check方法，并且传入rule/ruleSet/styleSheet作为参数，并且返回True(通过)/False(不通过)或错误信息数组

4、如果check返回bool值，则类中必须包含errorLevel和errorMsg属性，便于检测异常时给出错误提示

5、errorMsg中可以包含 ${selector}/${name}/${value}等属性设置，在错误提示时将进行相应替换

6、每一个规则，需要在tests目录中添加对应的单元测试用例，测试用例请参见"Unit Test"小节

### plugin Demo

``` python
from Base import *

class FEDSemicolonAfterValue(RuleChecker):
    def __init__(self):
        self.id = 'add-semicolon'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'each rule in "${selector}" need semicolon in the end, "${name}" has not'

    def check(self, rule):
        if not rule.strippedValue.endswith(';'):
            return False
        return True 
```

## Unit Test
每一个规则，都需要添加对应的单元测试

放置在tests/unit目录下的所有文件，都是单元测试用例文件（asserts.py和helper.py除外）

`tests/runUnitTests.py`是单元测试运行器，将运行tests/unit的所有单元测试并给出运行结果

### Python Unit Test
Python单元测试必须：

1、在文件中引入`asserts.py`，用于断言

2、在文件中加入`doTest`方法，并在doTest方法及其调用中编写断言

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
CSS的单元测试，必须满足以下条件：

1、必须包含`@unit-test-expecteds`，并在此规则中写入单元测试断言

2、每一个规则由key-value组成，key为错误的errorLevel，value为错误消息

3、如果断言中有，而实际检查结果中没有，测试时将出现`[expect but not have]`

4、如果断言中没有，而实际检查结果中有，测试时将出现`[unexpect but has]`

5、一定要注意errorLevel是否正确

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

## Rules(Plugins)
所有的规则都对应唯一id，并且有独立的检查类，所有的规则类都在`ckstyle/plugins`的`一级`目录下。

规则id、Python类与检查内容的对应关系(属性名为id，括号内为Python类名）如下：

<pre>
@all-rules {
    hexadecimal-color:              16进制颜色，大写，并且尽量省略 (FEDHexColorShouldUpper);
    no-font-family:                 不允许业务代码设置字体 (FEDCanNotSetFontFamily);
    combine-into-one:               将可以合并的样式设置合并 (FEDCombineInToOne);
    comment-length:                 注释长度不允许超过80个字符 (FEDCommentLengthLessThan80);
    css3-with-prefix:               css3前缀相关检查 (FEDCss3PropPrefix);
    css3-prop-spaces:               css3缩进相关检查 (FEDCss3PropSpaces);
    no-style-for-simple-selector:   不要为简单选择器设置样式，避免全局覆盖 (FEDDoNotSetStyleForSimpleSelector);
    no-style-for-tag:               不要为html tag设置样式 (FEDDoNotSetStyleForTagOnly);
    font-unit:                      字体的单位必须使用px或pt (FEDFontSizeShouldBePtOrPx);
    hack-prop:                      hack属性时的检查 (FEDHackAttributeInCorrectWay);
    hack-ruleset:                   hack规则时的检查 (FEDHackRuleSetInCorrectWay);
    high-perf-selector:             针对低性能的选择器的检查 (FEDHighPerformanceSelector);
    multi-line-brace:               代码多行时的括号检查 (FEDMultiLineBraces);
    multi-line-selector:            代码多行时的选择器检查 (FEDMultiLineSelectors);
    multi-line-space:               代码多行时的空格检查 (FEDMultiLineSpaces);
    add-author:                     需要在文件中添加作者信息 (FEDMustContainAuthorInfo);
    no-alpha-image-loader:          不要使用alphaImageLoader (FEDNoAlphaImageLoader);
    no-appearance-word-in-selector: 不要在选择器中出现表现相关的词汇 (FEDNoAppearanceNameInSelector);
    no-comment-in-value:            不要在css属性中添加注释 (FEDNoCommentInValues);
    no-empty-ruleset:               删除空的规则 (FEDNoEmptyRuleSet);
    no-expression:                  不要使用非一次性表达式 (FEDNoExpression);
    number-in-selector:             不要在选择器中使用简单数字1、2、3 (FEDNoSimpleNumberInSelector);
    no-star-in-selector:            不要在选择器中使用星号 (FEDNoStarInSelector);
    del-unit-after-zero:            删除0后面的单位 (FEDNoUnitAfterZero);
    no-zero-before-dot:             删除0.2前面的0 (FEDNoZeroBeforeDot);
    no-border-zero:                 用border:none替换border:0 (FEDReplaceBorderZeroWithBorderNone);
    no-underline-in-selector:       不要在选择器中使用下划线 (FEDSelectorNoUnderLine);
    add-semicolon:                  为每一个属性后添加分号 (FEDSemicolonAfterValue);
    do-not-use-important:           不要使用important (FEDShouldNotUseImportant);
    single-line-brace:              单行的括号检查 (FEDSingleLineBraces);
    single-line-selector:           单行的选择器检查 (FEDSingleLineSelector);
    single-line-space:              单行的空格检查 (FEDSingleLineSpaces);
    keep-in-order:                  属性应该按照推荐的顺序编写 (FEDStyleShouldInOrder);
    no-chn-font-family:             不要出现中文的字体设置，改用对应的英文 (FEDTransChnFontFamilyNameIntoEng);
    unknown-css-prop:               错误的css属性 (FEDUnknownCssNameChecker);
    unknown-html-tag:               错误的html tag (FEDUnknownHTMLTagName);
    lowercase-prop:                 属性应该用小写 (FEDUseLowerCaseProp);
    lowercase-selector:             选择器用小写字母 (FEDUseLowerCaseSelector);
    single-quotation:               使用单引号 (FEDUseSingleQuotation);
    z-index-in-range:               z-index取值应该符合范围要求 (FEDZIndexShouldInRange);
    remove-duplicated-attr:         删除重复的属性设置，取后面的(FEDRemoveDuplicatedAttr);
}
</pre>

## Join Us
Email: wangjeaf@gmail.com

Websites: <http://fed.renren.com/> | <http://www.renren.com/>
