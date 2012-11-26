from Combiner import Combiner
from helper import containsHack

class MarginCombiner(Combiner):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs
        self.combined = ''
        self.collector = {}
        self.deleted = []
        self.subs = ['left', 'top', 'bottom', 'right']
        self.initSubs()

    def initSubs(self):
        name = self.name
        for sub in self.subs:
            self.collector[name + '-' + sub] = ''

    def collect(self):
        name = self.name
        attrs = self.attrs
        for prop in attrs:
            if containsHack(prop[0], prop[1], prop[2]):
                break;

            if prop[1] == name:
                for direction in self.subs:
                    self.collector[name + '-' + direction] = prop[2]
            else:
                self.deleted.append(prop[1])
                self.collector[prop[0]] = prop[2]

    def join(self):
        left = self.collector[self.name + '-left']
        top = self.collector[self.name + '-top']
        right = self.collector[self.name + '-right']
        bottom = self.collector[self.name + '-bottom']

        if left == right == bottom == top:
            self.combined = left
        elif left == right and bottom == top:
            self.combined = '%s %s' % (top, left)
        elif top != bottom and left == bottom:
            self.combined = '%s %s %s' % (top, right, bottom)
        else:
            self.combined = '%s %s %s %s' % (top, right, bottom, left)

    def combine(self):
        self.collect()
        self.join()
        return self.combined, self.deleted

def combine(name, props):
    print MarginCombiner(name, props).combine()
    
if __name__ == '__main__':
    combine('margin', [
        ['margin', 'margin', '10px'],
        ['margin-left', 'margin-left', '0px'],
        ['margin-right', 'margin-right', '10px'],
        ['margin-top', 'margin-top', '10px'],
        ['margin-bottom', 'margin-bottom', '10px'],
        ['margin-bottom', 'margin-bottom', '30px']
    ])
