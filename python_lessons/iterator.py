import random


class Parent(object):

    def __init__(self, childs_count):
        self._current = -1 
        self._childs = []
        for i in range(childs_count):
            self._childs.append(random.randint(1, 10))

    def __str__(self):
        return "parent with %d childs" % len(self._childs)

    def __iter__(self):
        print "in __iter__"
        self._current = -1 
        return self

    def next(self):
        print "in next: %d" % self._current
        if self._current >= len(self._childs) - 1:
            raise StopIteration("finished")
        else:
            self._current += 1
            return self._childs[self._current]



class TaxRegulator(object):

    def __init__(self):
        super(TaxRegulator, self).__init__()

    def calculate_taxes(self, parent):
        taxes = 0

        # rule: if child age grater than 5 then tax += 1
        try:
            for child_age in parent:
                if child_age > 5:
                    taxes += 1

        except StopIteration, e:
            print "in exception %s" % e

        return taxes

p = Parent(5)
print p

t = TaxRegulator()
print "taxes %d" % t.calculate_taxes(p)
print "taxes %d" % t.calculate_taxes(p)