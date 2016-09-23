#include "test.h"
#include <fstream>
int main() {
    ofstream  outputFile;
    outputFile.open("outputFile.txt"); 
    test_class *myObj;
    myObj = new test_class();
    myObj->set_test_vars(2,3);
    myObj->print();
    cout<<*myObj;
    outputFile<<*myObj;
    outputFile.close();
}
