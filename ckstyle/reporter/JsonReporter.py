from .Reporter import Reporter
from .helper import fill
import json

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
        for error in errors:
            error["errorMsg"] = fill(error)
        for warn in warns:
            warn["errorMsg"] = fill(warn)
        for log in logs:
            log["errorMsg"] = fill(log)
            
        self.setMsg('{"errors":%s,"warnings":%s,"logs":%s}' % (json.dumps(errors), json.dumps(warns), json.dumps(logs)))

    def export(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg