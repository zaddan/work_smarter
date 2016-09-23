def myGenerator():
    number = 0 
    while(True): #generally have this line
        if (number >10):
            return #when a generator returns, it returns StopIteration Error
        yield number
        number += 1


mygen = myGenerator() #required to assign the function to a name

while(True):
    try:
        print next(mygen) #keep in mind that for generators, we use .next
                          #instead of next()
    except StopIteration:
        print "end of the generator"
        break

