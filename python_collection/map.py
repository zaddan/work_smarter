import operator
a = [3 for _ in range(10)]
b = [2 for _ in range(10)]
c = map(operator.mul , a,b)
print c


