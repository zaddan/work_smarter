try:
    fileP = open("ok", "r")
except IOError:
    print "this file is not found"


# ---- don't ever use the Exception as a general exception variable.
# ---- this might cause exception to silently propagate. Instead, you need to know
# ---- what kind of exception you are excepting. If you have to use the generic name,
# ---- to find out the name of the exception do the following

try:
    1/0 
except Exception as ex:
    print type(ex).__name__
    print ex.args
    exit()  # make sure to exit out if an exception happens, to avoid silent
            # propagation of the error   





