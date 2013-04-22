DEBUG = False
PREFIX = '[CKstyle %s] '

class console():

    @staticmethod
    def show(msg, t=""):
        if t != "":
            print(PREFIX % t + msg)
        else:
            print(msg)

    @staticmethod
    def showError(msg):
        console.show(msg, "ERROR")

    @staticmethod
    def showOk(msg):
        console.show(msg, "OK")

    @staticmethod
    def log(msg):
        if DEBUG:
            consle.show(msg, "LOG")

    @staticmethod
    def warn(msg):
        if DEBUG:
            console.show(msg, "WARN")

    @staticmethod
    def error(msg):
        if DEBUG:
            console.show(msg, "ERROR")
