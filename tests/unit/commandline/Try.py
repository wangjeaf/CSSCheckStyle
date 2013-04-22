from helper import *

def doTest():
    res = doFix([' ', 'fix', '-p', realpath('./_test.css')])
    expect = '''.test {
    width: 100px;
}'''
    equal(res, expect, 'fix by cmd line is ok')


    res = doCompress([' ', 'compress', '-p', realpath('./_test.css')])
    expect = '''.test{width:100px}'''
    equal(res, expect, 'compress by cmd line is ok')

    res = doCompress([' ', 'compress', '-p', realpath('./_test_browsers.css')])
    expect = '''.test{width:100px}.test[prop]{width:100px}'''
    equal(res, expect, 'compress by cmd line is ok')

    res = doCompress([' ', 'compress', '-p', '--browsers=ie6', realpath('./_test_browsers.css')])
    expect = '''.test{width:100px}'''
    equal(res, expect, 'compress by cmd line ie6 is ok')

    res = doCompress([' ', 'compress', '-p', '--browsers=ie7', realpath('./_test_browsers.css')])
    expect = '''.test{width:100px}.test[prop]{width:100px}'''
    equal(res, expect, 'compress by cmd line ie7 is ok')