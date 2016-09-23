#include <iostream>
class superClass {
  public: 
      int a;
      int b;
      int addObj(superClass a, superClass b);
};

int superClass::addObj(superClass a, superClass b) {
   return a.a + b.b;
}

class subClass: public superClass{
    public: 
        int c;

    int addObj(subClass a, subClass b);
};
int subClass::addObj(subClass a, subClass b) {
   return a.a + b.b;
}



int main() {
    subClass B;
    B.c = 1;
    B.a = 2;
    B.b = 3;

    superClass A;
    A.a = 20;
    A.b = 30;
   
    superClass *C = new superClass();
    C->a = 20;
    C->b = 30;
    


    std::cout<<A.addObj(B, A); //this would work b/c B get's promoted to subClass
    
    //std::cout<<B.addObj(B, A); //this won't work b/c A can not be demoted implicitly
    
    //we can use static casting to do so, but dynamic casting is only applicable for refrences.
    std::cout<<B.addObj(B, *static_cast<subClass*>(C)); //this won't work b/c A can not be demoted implicitly
}
