from .TextReporter import TextReporter
from .JsonReporter import JsonReporter
from .XMLReporter import XMLReporter

class ReporterUtil():
    @staticmethod
    def getReporter(reporterType, checker):
        if reporterType == 'text':
            return TextReporter(checker)
        elif reporterType == 'json':
            return JsonReporter(checker)
