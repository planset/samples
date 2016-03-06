
import random

def random_weight_choice(L):
    choice = None
    total = 0

    for item, p in L:
        total += p
        if random.random() * total < p:
            choice = item

    return choice

def test_random_weight_choice():
    from collections import defaultdict

    X = [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
    count = defaultdict(int)

    for _ in xrange(100000):
        item = random_weight_choice(X)
        count[item] += 1

    print count

if __name__ == '__main__':
    test_random_weight_choice()
