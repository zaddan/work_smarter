from all_funcs import *
import sympy
def foo(a,b):
    return a*b + a + b
x = [] 
for index in range(2):
    x.append([])
y = sympy.symbols('x[0] x[1]')
print y[0]
print y[1]
e = foo(*y)
print e
print e.subs(y[0], 2)
print e
print e.diff(y[0])

# result = degreeNPolyMultiVar([2,a,b], [1,2,1])
# print result

