#!/usr/bin/env python
import sys
import os
def complete_DB_creation(sourceFileName, desFileAddress):
    
    resultFile = desFileAddress
    resultP= open(resultFile, "w") 
    # if not(os.path.isfile(sourceFileName)):
        # print "the source file doesn't exist"
        # exit();
    try:
        f = open(sourceFileName)
        props = [] 
    except IOError:
        handleIOError(sourceFileName, "csource file")
        exit()
    else:
        with f:
            for line in f:
                for words in line.replace(',', ' ').replace('/',' ').replace(';', ' ').split(' '): #find the lines with key word and write it to another file
                    if words != " ": 
                        props.append(str(words))
                        break
        resultP.write( "dbFileName = ????\n" )
        resultP.write( "tableName = ????\n")
        
        stringToWrite = 'propsName = ['
        for index,prop in enumerate(props):
            if not(index == len(props) - 1):
                stringToWrite += '"' + str(prop)+ '", '
            else:
                stringToWrite += '"' + str(prop)+ '"]'
        resultP.write( stringToWrite + "\n")
                    
        resultP.write( "propsType = ????\n" )


        stringToWrite = 'propList = ['
        for index,prop in enumerate(props):
            if not(index == len(props) - 1):
                stringToWrite += ' ' + str(prop)+ ', '
            else:
                stringToWrite += ' ' + str(prop)+ ']'

        resultP.write( stringToWrite + "\n")

        resultP.write("\n# ----body \n")
        stringToWrite = "propsTypeConverted = [convert_python_types_to_sqlite(argType) for argType in propsType]"
        resultP.write( stringToWrite + "\n")
        stringToWrite = "propsValuesConverted = [convert_python_values_to_sqlite_compatible_values(argType,value) for argType,value in zip(propsType,propList)]"
        resultP.write( stringToWrite + "\n")
        resultP.write("\n# ---- creating  \n")
        stringToWrite = "createDB(dbFileName, tableName, propsName, propsTypeConverted, propsValuesConverted)"
        resultP.write(stringToWrite + "\n")
        resultP.close()
    return props

def complete_DB_reteive(props, desFileAddress):
    resultFile = desFileAddress 
    resultP= open(resultFile, "a") 
    resultP.write("\n\n")
    resultP.write("# ---- retreiving\n")
    resultP.write("props, propNames, _= retrieveDB(dbFileName , tableName)")
    stringToWrite ='\n' 
    for index,prop in enumerate(props):
        if not(index == len(props) - 1):
            stringToWrite +=  str(prop)+ ', '
        else:
            stringToWrite +=  str(prop)+ ' '
    resultP.write( stringToWrite )
         
    stringToWrite = " = [impose_type(propsType[index], prop) for index,prop in enumerate(props)]"
    
    resultP.write(stringToWrite)    
    
    resultP.write("\n\n")
    for index in range(len(props)): 
        resultP.write("print " + props[index] + " \n")
    
    resultP.close()

def main():
    print """you need to have defined each one of the props. For example, if the props
    of interests are operatrorNumber and lowerBound varlues, we need to have
    defined them in a list of their own. For example:
    operatroNumber = [1,2]
    lowerBound = [0, 1]"""
    srcFileName = raw_input("name of the file to get the props from: ")
    desFileName = raw_input("name of the file to store the result in: ")
    baseAddress = raw_input("baseAddress: ")
    retrieve = raw_input("do you want the retrieve ass well: ")
    srcFileFullAddress = baseAddress + "/" + srcFileName
    desFileFullAddress = baseAddress + "/" + desFileName
    props = complete_DB_creation(srcFileFullAddress, desFileFullAddress)
    if retrieve in ["YES", "yes"]:
        complete_DB_reteive(props, desFileFullAddress)
     


main()
