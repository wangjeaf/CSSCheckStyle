from Reporter import Reporter

class TextReporter(Reporter):
    def __init__(self, checker):
        self.checker = checker
        self.msgs = []
        pass

    def doReport(self):
        checker = self.checker
        counter = 0
        formatter = '%s %s. %s'

        logs, warns, errors = checker.errors()
        if len(logs) == 0 and len(warns) == 0 and len(errors) == 0:
            self.appendMsg('aha, no problem')
            return

        for error in errors:
            counter = counter + 1
            self.appendMsg(formatter % ('[ERROR]', counter, error))
        for warn in warns:
            counter = counter + 1
            self.appendMsg(formatter % (' [WARN]', counter, warn))
        for log in logs:
            counter = counter + 1
            self.appendMsg(formatter % ('  [LOG]', counter, log))

    def appendMsg(self, msg):
        self.msgs.append(msg)

    def export(self):
        return '\n'.join(self.msgs)
