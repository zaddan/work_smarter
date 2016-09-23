# ---- hello world example
a = range(10)

aIter = iter(a)
print aIter.next() #note that .next instead of next(foo name) is use for
                  #iterators as opposed to generators

while(True):
    try: 
        print aIter.next()
    except StopIteration:
        print "end of iteration"
        break



