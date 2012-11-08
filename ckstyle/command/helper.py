import string

def getValue(txt):
    sp = txt.split(':')
    if len(sp) == 1:
        print '[ConfigError] no value after semicolon(:) '
    return sp[1].strip()

def getNumber(txt):
    value = None
    try:
        value = string.atoi(txt)
    except ValueError:
        pass
    return value

class ExportMode():
    NONE = 0
    SEPERATE = 1
    ONE_FILE = 2
    CONSOLE = 3

    @staticmethod
    def getMode(txt):
        mode = None
        if value == '-n':
            mode = ExportMode.NONE
        elif value == '-a':
            mode = ExportMode.ONE_FILE
        elif value == '-p':
            mode = ExportMode.CONSOLE
        elif value == '-s':
            mode = ExportMode.SEPERATE
        return mode
