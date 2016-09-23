from all_funcs import *
import sympy
def foo(a,b):
    return a*b + a + b

a=sympy.Symbol('a')
b=sympy.Symbol('b')
e = foo(a,b)
print e
print e.diff(a)
# result = degreeNPolyMultiVar([2,a,b], [1,2,1])
# print result

