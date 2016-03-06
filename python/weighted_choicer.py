import random
import bisect

class Choicer(object):

    def __init__(self, L):
        total = 0
        self.probs = []
        self.items = []

        for item, p in L:
            total += p
            self.probs.append(total)
            self.items.append(item)

    def choice(self):
        r = random.random() * self.probs[-1]
        idx = bisect.bisect(self.probs, r)
        return self.items[idx]

def test_random_weight_choice():
    from collections import defaultdict

    X = [('A', 3), ('B', 2), ('C', 5)]
    choicer = Choicer(X)
    count = defaultdict(int)

    for _ in xrange(100000):
        item = choicer.choice()
        count[item] += 1

    print count

if __name__ == '__main__':
    test_random_weight_choice()

