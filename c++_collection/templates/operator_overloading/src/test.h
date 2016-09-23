#include <iostream>
using namespace std;

class test_class{
    int test_var1; 
    int test_var2; 
    public:
    test_class() {};
    void set_test_vars(int, int);
    void print();
//    friend ostream& operator<<(ostream &out, test_class obj){ //wasn't able to define this in .cpp
//        out<<"var1: "<<obj.test_var1<<"\n";
//        out<<"var2: "<<obj.test_var2<<"\n";
//        return out;  
//   }

    friend std::ostream& operator<<(std::ostream &out, const test_class &obj);
//        out<<"var1: "<<obj.test_var1<<"\n";
//        out<<"var2: "<<obj.test_var2<<"\n";
//        return out;  
//   }

};
