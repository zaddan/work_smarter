#---user defined exceptions
#---simply defined a class 
class ValueTooSmall(Exception):
    pass

class ValueTooLarge(Exception):
    pass

class ValueTooLargeTopLevel(Exception):
    pass
class GeneralTopLevelError(Exception):
    def __init__(self, error_name):
        self.error_name = error_name



#---- use if statements to check the santity of the program and (force) raise 
#---- exceptions if the sanity check fails
def foo(x):
    try:
        if x > 100:
            raise ValueTooLarge
        if x < -100:
            raise ValueTooSmall
    except ValueTooSmall:
        print "this value: " + str(x) +" is too small"
        exit()
    except ValueTooLarge:
        print "this value: " + str(x) + " too large"
        exit()
    finally:
        print "was in foo"

#-----user defined error/exceptions
def example_1():
    while True:
        input_var = int(raw_input('provide the num: '))
        if (input_var == 999):
            break
        foo(input_var)


#---- system defined errors/exceptions
def example_2():
    #----already existing errors"
    try:
        x = 1/0
    except ZeroDivisionError as err:
        print ("zero division error is happeneing", err)
    except NameError as err:
        print ("name error is happeneing", err)
    except:
        print ("other errors are happening")
    finally:
        print "dont with this"
    for x in range(0,10):
        print x

    
#--- the case for hierarchical exceptions
def foo_2(x):
    try:
        if x > 100:
            raise ValueTooLarge
    except ValueTooLarge:
        print "the x value: " + str(x) + " too large"
        raise ValueTooLargeTopLevel 
    finally:
        print "was in foo_2"

def foo_top(x, y):
    try: 
        foo_2(x)
    except ValueTooLargeTopLevel:
        print("the y value was:",y)

def example_3():
    while True:
        input_var_1 = int(raw_input('provide the num: '))
        input_var_2 = int(raw_input('provide me ANOTHER the num: '))
        if (input_var_1 == 999 or input_var_2 == 999):
            break
        foo_top(input_var_1, input_var_2)



#--- the case for hierarchical exceptions with variables
def foo_4(x):
    try:
        if x > 100:
            raise ValueTooLarge
    except ValueTooLarge as er:
        print "the x value: " + str(x) + " too large"
        raise GeneralTopLevelError(type(er).__name__)
    finally:
        print "was in foo_2"

def foo_top_2(x, y):
    try: 
        foo_4(x)
    except GeneralTopLevelError as er:
        print("error name is", er.error_name) 

def example_4():
    while True:
        input_var_1 = int(raw_input('provide the num: '))
        input_var_2 = int(raw_input('provide me ANOTHER the num: '))
        if (input_var_1 == 999 or input_var_2 == 999):
            break
        foo_top_2(input_var_1, input_var_2)






def main():
#    example_1()
#    example_2()
#     example_3()
    example_4()



if __name__ == "__main__":
    main()


