import numpy as np
import itertools
import os
import sys

# ---- finding index
[1,4,5].index(4) #for inding index

# ---- making a dictionary out of lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print dictionary


# ---- zipping and unzipping
l1 = [1,4,5]
l2 = [10,40, 50]
l3 = zip(l1,l2)

# ---- how to unzip back to the original lists
l4 = zip(*l3)
l4 = map(list, l4)
print l3
print l4

# ---- vectorizing a function
def myFunc1(x):
    return x**2

vMyFunc1 = np.vectorize(myFunc1)
print vMyFunc1(range(4))

def myFunc2(x,y):
    return x*y

vMyFunc2 = np.vectorize(myFunc2)
print vMyFunc2(range(4), range(3,7))
print vMyFunc2(range(4), 2)

# ---- we can use map to do the same as vectorization as above
result = map(lambda x: myFunc2(*x), zip(range(4), range(3,7)))
print result


# ---- use itertools.product to permute. Then use map to pass the tuples to the
# functions
resultsPermuted = list(itertools.product(range(4), range(7,11)))
result = map(lambda x: myFunc2(*x), resultsPermuted)
print result

# ---- difference between iteritems and items.
# ---- items() return a list of (k,v) tuples, where as iteritems() is a
# generator, thus it yields a tuple. the difference is in memory consumption
a = {1:'t', 2:'y'}
for element in a.iteritems():
    print element
print a.items()




# ---- name tuples
from collections import namedtuple
operator = namedtuple("operator", ["operand1", "operand2", "deltaOperand1"])
operator1 = operator(1,4,2)
print operator1.operand1
print operator1.operand2

# ---- going from lists to name tuples
operand1 = [1,2,3]
operand2 = [10,20,30]
deltaOperand1 = [7,8,9]
lOfOperators = map(lambda x : operator(*x), zip(operand1, operand2, deltaOperand1))
print lOfOperators




# ---- counters
from collections import Counter
l = [(1,2), (3,4) , (1,2), (4,5)]
c = Counter(l)
print c
print c[(1,2)]


