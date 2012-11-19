import string
from ckstyle.cmdconsole.ConsoleClass import console

def getValue(txt):
    sp = txt.split(':')
    if len(sp) == 1:
        console.error('[ConfigError] no value after semicolon(:) ')
    return sp[1].strip()

def getNumber(txt):
    value = None
    try:
        value = string.atoi(txt)
    except ValueError:
        pass
    return value
