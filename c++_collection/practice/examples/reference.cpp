#include <string.h>
#include <stdio.h>
#include <sstream>    
#include <iostream>
using namespace std;
int foo(int &x){
    x += 1;
}

int foo2(float &x){
    x += 1;
}
int main(){
    int y = 3;
    cout <<y <<endl;
    foo2((float)y); 
    //foo2(dynamic_cast<float>(&y));
    cout <<y <<endl;
    return 0;
}
