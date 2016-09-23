everytime you use os.system command, make sure to get the error and error out

use m and the first row for special cases
make a knowlege file in other folders

to debug, if you want to print and exit, use sys.exit, but other time use exit. this is a way to distinguish between the two


to iterate through items of a dictionary use:
for key,value in dicName.item():


how to generate a dictionary on the spot
funcErrorDic = {key: math.sqrt(sum(square(value))) for  key,value in
dicName.items()}



# ---- 
To be able to run a python file using ./:
add the following line to the beginiing of the file
#!/usr/bin/python

# ---- 
to get cscope work with pythong files do the following
 find . -name '*.py' > cscope.files
cscope -R
