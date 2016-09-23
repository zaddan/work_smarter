def sourceFileParse(sourceFileName, lAllOpsInSrcFile):
    # if not(os.path.isfile(sourceFileName)):
        # print "the source file doesn't exist"
        # exit();
    try:
        f = open(sourceFileName)
    except IOError:
        handleIOError(sourceFileName, "csource file")
        exit()
    else:
        with f:
            for line in f:
                for words in line.replace(',', ' ').replace('/',' ').replace(';', ' ').split(' '): #find the lines with key word and write it to another file
                   do something 
