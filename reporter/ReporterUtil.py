from TextReporter import TextReporter
from XMLReporter import XMLReporter

class ReporterUtil():
    @staticmethod
    def getReporter(reporterType, checker):
        if reporterType == 'text':
            return TextReporter(checker)
        else:
            return XMLReporter(checker)
