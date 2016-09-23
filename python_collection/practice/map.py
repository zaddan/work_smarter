from pprint import pprint

# ---- using map with a multivariable function
def foo(x,y):
    print x,y,"hwllo"
map(lambda x: foo(*x), zip(range(4), range(5,9)))


# ---- using pprint to print values in a list. print doesn't work in map
list(map(pprint, range(4)))



