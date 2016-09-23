import os
import sys

def sourceFileParse(sourceFileName):
    try:                                                                        
        f = open(sourceFileName)                                                
    except IOError:                                                             
        print sourceFileName + " file not found"
        sys.exit(0); 
        #exit()                                                                  
    else:                                                                       
        with f:                                                                 
            for line in f:                                                      
                for word in line.split():
                    print word
                    
def main():
    inputFileName = "/home/polaris/behzad/behzad_local/sd-vbs/benchmarks/sift/data/sim/expected_C.txt"
    sourceFileParse(inputFileName)
    
main()
