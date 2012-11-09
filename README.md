CSSCheckStyle
=============
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

## Complete Example
<pre>
ckstyle -c xxx.ini -r -p -c xxx.ini --extension=.test.txt --include=all --exclude=none --errorLevel=2 dirpath
</pre>

## Options
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

## CommandLineOptions
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

## Priority
指定的配置项的优先级：
**命令行参数 > 指定的配置文件中的配置 > 默认配置文件路径的配置 > 工具的默认参数**

## Description
<pre>
@description {
	destination: 检查代码中的不符合CSS编码规范的问题，并给出错误提示;
	reference: 人人FED CSS编码规范;
	check-result: 默认将第一个文件的异常打印出，同时为每一个存在异常的检查文件生成错误信息文件，放在源文件相同目录下;
	check-result-file-name: 文件名+.ckstyle.txt，例如a.css的异常文件名为a.css.ckstyle.txt;
	check-result-extra: -p为所有结果打印到控制台，-a为所有异常输出到同一个文件中;
	language: python;
}
</pre>

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

## Join us
欢迎使用，并参与到开发当中来。
<pre>
@author-info {
    author: zhifu.wang;
    email: wangjeaf@gmail.com;
}
</pre>
