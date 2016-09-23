#include "test.h"
void test_class::set_test_vars(int var1, int var2) {
    test_var1 = var1;
    test_var2 = var2;
}

void test_class::print(){
    cout<<test_var1<<" "<<test_var2<<endl;
}

ostream& operator<<(ostream &out, const test_class &obj){//{ //wasn't able to define this in .cpp
    out<<"var1: "<<obj.test_var1<<"\n";
    out<<"var2: "<<obj.test_var2<<"\n";
    return out;  
}
