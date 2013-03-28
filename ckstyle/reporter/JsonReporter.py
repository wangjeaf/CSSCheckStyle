from Reporter import Reporter

class JsonReporter(Reporter):
    def __init__(self, checker):
        self.checker = checker
        self.msg = ''
        pass

    def doReport(self):
        checker = self.checker
        counter = 0
        formatter = '%s'

        logs, warns, errors = checker.errors()
        if len(logs) == 0 and len(warns) == 0 and len(errors) == 0:
            self.setMsg('{}')
            return
        self.setMsg('{"errors":%s,"warnings":%s,"logs":%s}' % (
            ('[' + ','.join([('"' + x.replace('"', '\\"') + '"') for x in errors if not x.startswith('"')]) + ']') if len(errors) != 0 else 'null', 
            ('[' + ','.join([('"' + x.replace('"', '\\"') + '"') for x in warns if not x.startswith('"')]) + ']') if len(warns) != 0 else 'null', 
            ('[' + ','.join([('"' + x.replace('"', '\\"') + '"') for x in logs if not x.startswith('"')]) + ']') if len(logs) != 0 else 'null'))

    def export(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg