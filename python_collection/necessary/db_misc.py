import os
import sys
import sympy
def impose_type(argType, argList):
    result = []     
    if (argType in ["text", "string"]):
        return [str(arg) for  arg in argList ]
    elif (argType in ["int", "INTEGER", "integer"]):
        return [int(arg) for  arg in argList]
    elif (argType in ["REAL", "float"]):
        return [float(arg) for  arg in argList]
    elif (argType in ["tuple"]):
        return [eval(arg) for  arg in argList]
    elif ("mix" in argType):
        tempResult = [] 
        for element in argList:
            tempResult +=[element]
        return tempResult 
    elif ("list" in argType):
        for element in argList:
            tempResult = [] 
            if (argType in ["listString"]):
                tempResult += [element]
            if (argType in ["listInteger", "listInt"]):
                tempResult +=eval(element)
            elif (argType == "listFloat"):
                tempResult +=eval(element)
            elif (argType in ["listTuple"]):
                tempResult +=eval(element)
            elif (argType == "listFloats"):
                tempResult +=eval(element)
            elif (argType == "listList"):
                tempResult +=eval(element)
            else: 
                print "this type: " + str(argType) + " does not exist"
            result +=[tempResult]     
        return result 
    else:
        print "this type: " + str(argType) + " does not exist"
        exit()

def convert_python_types_to_sqlite(argType):
    if (argType == "string"):
        return "text"
    if (argType == "tuple"):
        return "text"
    elif (argType in [ "listInteger", "listInt"]):
        return "text" 
    elif (argType == "listFloat"):
        return "text" 
    elif (argType == "listList"):
        return "text" 
    elif (argType == "mix"):
        return "text" 
    elif (argType == "listString"):
        return "text" 
    elif (argType == "listTuple"):
        return "text" 
    elif (argType == "list"):
        return "string"
    elif (argType == "text"):
        return "text"
    elif (argType == "int"):
        return "int"
    elif (argType == "float"):
        return "REAL"
    elif (argType == "REAL"):
        return "REAL"
    elif (argType == "integer"):
        return "INTEGER"
    else:
        print "this type: " + str(argType) + " is not convertible"
        exit()

def convert_python_values_to_sqlite_compatible_values(argType, argValues):
    if (argType == "string"):
        return argValues
    elif (argType in "mix"):
        result = []   
        for element in argValues:
            result.append(str(element))
        return result 
    elif (argType in ["listInteger", "listInt"]):
        result = []   
        for element in argValues:
            result.append(str(element))
        return result
    elif (argType == "listFloat"):
        result = []  
        for element in argValues:
            result.append(str(element))
        return result
    elif (argType == "listString"):
        result = []  
        for element in argValues:
            result.append(str(element))
        return result
    elif (argType == "tuple"):
        result =[] 
        for element in argValues:
            result.append(str(element))
        return result 
    elif (argType == "listTuple"):
        result = []  
        for element in argValues:
            result.append(str(element))
        return result
        # propListTemp = []  
        # for element in argValues:
            # temp = [] 
            # for item in element:
                # temp += [str(item).replace(' ', '')]

            # propListTemp.append(' '.join(temp))
        # return propListTemp 
    elif (argType == "listList"):
        result = []  
        for element in argValues:
            result.append(str(element))
        return result
    elif (argType == "text"):
        return argValues 
    elif (argType == "int"):
        return argValues 
    elif (argType == "float"):
        return argValues 
    elif (argType == "REAL"):
        return argValues 
    elif (argType == "integer"):
        return argValues 
    else:
        print "this type: " + str(argType) + " is not convertible"
        exit()


