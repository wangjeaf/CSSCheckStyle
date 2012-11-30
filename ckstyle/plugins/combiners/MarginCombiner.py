from Combiner import Combiner
from helper import containsHack

class MarginCombiner(Combiner):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs
        self.combined = ''
        self.collector = {}
        self.deleted = []
        self.hasFather = False
        self.subs = ['left', 'top', 'bottom', 'right']
        self.initSubs()

    def initSubs(self):
        name = self.name
        for sub in self.subs:
            self.collector[name + '-' + sub] = ''

    def _seperate(self, value):
        splited = value.split(' ')
        top = right = bottom = left = ''
        length = len(splited)
        if length == 1:
            top = right = bottom = left = value
        elif length == 2:
            top = bottom = splited[0].strip()
            left = right = splited[1].strip()
        elif length == 3:
            top = splited[0].strip()
            left = right = splited[1].strip()
            bottom = splited[2].strip()
        elif length >= 4:
            top = splited[0].strip()
            right = splited[1].strip()
            bottom = splited[2].strip()
            left = splited[3].strip()
        name = self.name
        self.collector[self.name + '-top'] = top
        self.collector[self.name + '-right'] = right
        self.collector[self.name + '-bottom'] = bottom
        self.collector[self.name + '-left'] = left

    def collect(self):
        name = self.name
        attrs = self.attrs
        for prop in attrs:
            if containsHack(prop[0], prop[1], prop[2]):
                break;

            if prop[1] == name:
                self.hasFather = True
                self._seperate(prop[2])
            else:
                if not prop[1] in self.deleted:
                    self.deleted.append(prop[1])
                self.collector[prop[0]] = prop[2]

    def join(self):
        left = self.collector[self.name + '-left']
        top = self.collector[self.name + '-top']
        right = self.collector[self.name + '-right']
        bottom = self.collector[self.name + '-bottom']

        if left == '' or top == '' or right == '' or bottom == '':
            self.combined = None
            self.deleted = []
            return

        if left == right == bottom == top:
            self.combined = left
        elif left == right and bottom == top:
            self.combined = '%s %s' % (top, left)
        elif top != bottom and left == right:
            self.combined = '%s %s %s' % (top, right, bottom)
        else:
            self.combined = '%s %s %s %s' % (top, right, bottom, left)

    def combine(self):
        self.collect()
        self.join()
        return self.combined, self.deleted, self.hasFather
