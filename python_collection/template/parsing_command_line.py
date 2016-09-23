#!/usr/bin/env python

from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-x", "--xhtml",
                      action="store_true",
                      dest="xhtml_flag",
                      default=False,
                      help="create a XHTML template instead of HTML")
    parser.add_option("-c", "--cssfile",
                      action="store", # optional because action defaults to "store"
                      dest="cssfile",
                      default="style.css",
                      help="CSS file to link",)
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    #printing the options 
    print options 
    #note: note that we can get the value of an option by simply doing options.(nameOfTheOptionDes) 
    print options.cssfile
    print options.xhtml_flag    
    #printing the positional arguments  (what is left over after parsing the options)
    print args

if __name__ == '__main__':
    main()
