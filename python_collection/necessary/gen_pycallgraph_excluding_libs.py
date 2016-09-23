#!/usr/bin/env python
import os
def sourceFileParse(sourceFileName):
    libList = [] 
    try:
        f = open(sourceFileName)
    except IOError:
        handleIOError(sourceFileName, "csource file")
        exit()
    else:
        with f:
            for line in f:
                for words in line.replace(',', ' ').replace('/',' ').replace(';', ' ').split(' '): #find the lines with key word and write it t
                    libList.append(words)

    return libList

def main():
    stringsToOutput = '' 
    
    print "give me the baseDirectory Address"
    print "------Note:This address is used as the base address for the rest of inupts."
    print "-----------This directory is almost always the one that you are in. "
    print "-----------so use pwd to get this address and pass it in: "

    baseDir =  raw_input()
    targetFileRelativeAddress = raw_input("relative address(with respect to the base) of the file to implement pycallgraph on: " )
    assert(os.path.isdir(baseDir), "the directory with the name: " + baseDir + " does not exist") 
     
    libFileRelativeAddress = raw_input("relative address of the libToExclude File containing the libs to exclude: ")
    outputFileRelativeAddress = raw_input("relative address of outputFileAddress: " )
    
    targetFileFullAddress = baseDir + "/" + targetFileRelativeAddress
    libFileFullAddress = baseDir + "/" + libFileRelativeAddress
    outputFileFullAddress = baseDir + "/" + outputFileRelativeAddress
    
    assert(os.path.isfile(targetFileFullAddress)), "the file with the address " + str(targetFileFullAddress) + " does not exist"
    assert(os.path.isfile(libFileFullAddress)), "the file with the address " + str(libFileFullAddress) + " does not exist"
    
    libsToExclude = sourceFileParse(libFileFullAddress)
    for libs in libsToExclude:
        stringsToOutput += "-e " + libs + " "
   
    
    # print "pycallgraph " + stringsToOutput.rstrip() +  " " + "graphviz -f svg -o " + outputFileFullAddress + " " + targetFileFullAddress
    os.system("pycallgraph " + stringsToOutput.rstrip() +  " " + "graphviz -f svg -o " + outputFileFullAddress + " " + targetFileFullAddress)
main()
