DEBUG = False

class console():
    @staticmethod
    def show(msg):
        print(msg)

    @staticmethod
    def log(msg):
        if DEBUG:
            print('[console.log] %s' % msg)

    @staticmethod
    def warn(msg):
        if DEBUG:
            print('[console.warn] %s' % msg)

    @staticmethod
    def error(msg):
        if DEBUG:
            print('[console.error] %s' % msg)
