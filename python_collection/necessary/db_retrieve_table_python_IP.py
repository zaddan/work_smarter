import sqlite3
import copy
from db_misc import *

def get_prop_name(propertyTuple):
    return str(propertyTuple[1]) 

def get_prop_type(propertyTuple):
    return str(propertyTuple[2])

def get_prop_index(propertyTuple):
    return propertyTuple[0] 

def retrieveDB(fileName, tableName):
    assert(os.path.isfile(fileName)), str(fileName) + " does not exist" 
    conn = sqlite3.connect(fileName)
    c = conn.cursor()
    c.execute("select * from " + tableName)
    result = c.fetchall()


    propIndex = []
    propType = []
    propNames = []

    # ---- meta info necessary for finding out the prop types
    meta = c.execute("PRAGMA table_info('" + tableName +"')")
    for propTuple in meta:
        propNames.append(get_prop_name(propTuple))

    
    meta = c.execute("PRAGMA table_info('" + tableName +"')")
    for propTuple in meta:
        propType.append(get_prop_type(propTuple))

    
    meta = c.execute("PRAGMA table_info('" + tableName +"')")
    for propTuple in meta:
        propIndex.append(get_prop_index(propTuple))


    for propName in propNames[1:]:
        exec(propName + " = []")
        print propName

    mydic = {}
    # funcName.append("what")
    # print funcName
    for element in result:
        for index, propName in enumerate(propNames[1:]):
            exec(propName +".append(str(element[index+1]))")
            # exec(propName +".append('"+ str(element[index+1]) +"')")
    props = [eval(prop) for prop in propNames[1:]]

    return props, propNames[1:], propType


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---- testing
def test():
    # ---- necessary inputs
    dbfilename = "example.db"
    tablename = "persons"
    # ---- get this from the module that calles createDB
    propstype = ["text"]*2 +["liststring"] + ["float"] + ["listfloat"]
    
    # ---- body (copy past only the line bellow)
    props, propNames, propType = retrieveDB(dbFileName, tableName)
    # names, city, friends, age = [impose_type(propType[index + 1], prop) for index,prop in enumerate(props)]
    
    # ---- this line changes based on the properties
    names, city, friends, age, numberOfSiblings = [impose_type(propsType[index], prop) for index,prop in enumerate(props)]


# doTest = True
doTest = False 
if (doTest):
    test()

# for prop in propNames[1:]:
    # print prop 
    # myList =  eval(prop)
# print myList
