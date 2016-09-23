import os
import sqlite3
import sys
from db_misc import *


# ---- props format : propeties Names, variableNames, other property values
def createDB(fileName, tableName, propsNames, propsType, props):
    # for propertyName in propsNames:
        # exec(propertyName + " = []")
        
    # for propertyName, propertyValues in zip(propsNames, props):
        # for value in propertyValues: 
            # exec(propertyName +".append('"+ str(value) +"')")

    # ---- create a file if it doesnt exist
    if os.path.exists(fileName): 
        try: 
            os.remove(fileName)
        except Exception:
            print "was not able to remove the " + str(fileName) 
        else:
            print "removing the previous file"
    conn = sqlite3.connect(fileName)
    c = conn.cursor()
        
    stringToWrite = "(id int "
    for propName,propType in zip(propsNames, propsType):
        stringToWrite += ", " + str(propName) + " " + str(propType) 
    stringToWrite += ")"
    c.execute('create table ' + str(tableName) + " " + stringToWrite)

    
    
    ltableInfo = zip(range(len(props[0])), *props)
    print "ltableInfo : " + str(ltableInfo )
    
    for element in ltableInfo:
        c.execute('insert into ' + str(tableName) + " VALUES " + str(element))

    conn.commit()
    conn.close()

    # ltableInfo = zip(range(len(names)), names,city, friends)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---- test
def test():
    # ---- necessary inputs
    
    dbFileName = "example.db"
    tableName = "Persons"
    
    # ---- type of properties to consider.
    # ---- Note: name can be just number. Names represent the object
    propsName =  ["names", "city", "friends", "age", "numberOfSiblings"]
    propsType = ["text"]*2 +["listString"] + ["float"] + ["listFloat"]
    
    names = ["behzood", "molly"]
    city = ["ramsar", "portland"]
    mollyFriend = ["crystal", "crystin", "nathan"]
    behzadFriend = ["luke", "brett", "daniel"]
    friends = [mollyFriend, behzadFriend]
    age = [27.2,26.3] 
    numberOfSiblings = [[1,1], [1,0]]
    
    # ---- body (copy paste the rest)
    propsTypeConverted = [convert_python_types_to_sqlite(argType) for argType in propsType]
    propList = [names, city, friends, age, numberOfSiblings]
    for index, argType in enumerate(propsType):
        if "list" in argType:
            propList[index] = [' '.join(map(str, element)) for element in propList[index]] 
    createDB(dbFileName, tableName, propsName, propsTypeConverted,propList)


# doTest = True
doTest = False 
if (doTest):
    test()

