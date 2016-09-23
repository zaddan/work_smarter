#include <iostream>
#include<algorithm>
#include <vector>
#include <assert.h>
using namespace std;

//typedef struct 
//{
//    unsigned short int gender; //0 = male | 1 = female
//    unsigned short int age;
//    int index;
//}record;
//

typedef struct 
{
    unsigned short int cold_count; //0 = male | 1 = female
    unsigned short int hot_count;
    unsigned short int fine_count;
    unsigned short int E_count;
    unsigned short int M_count;
    unsigned short int S_count;
    unsigned short int O_count;
    unsigned short int active;
    unsigned short int I_count;
    
    int index;
}record;







bool CompareRecords(const record& a, const record& b)
{
    

    if (a.active == 0) {
        return true;
    }
    if (b.active == 0) {
        return false;
    }
    
    if (a.cold_count+ a.I_count+a.fine_count < b.cold_count+b.I_count+b.fine_count)
        return true;
    if (a.cold_count+ a.I_count+a.fine_count > b.cold_count+b.I_count+b.fine_count)
        return false;

    if (a.hot_count > b.hot_count)
        return true;
    if (a.hot_count < b.hot_count)
        return false;

    if (a.S_count < b.S_count)
        return true;
    if (a.S_count > b.S_count)
        return false;

    if (a.E_count < b.E_count)
        return true;
    if (a.E_count > b.E_count)
        return false;

    if (a.M_count < b.M_count)
        return true;
    if (a.M_count > b.M_count)
        return false;
    
    return false;
}
int main() {

    int num_set_per_slice = 6; 
    std::vector<record> X(num_set_per_slice);
    
    for(int i =0; i <num_set_per_slice; i++) {
        X[i].index = i;
    }
   

    X[0].cold_count = 3;
    X[0].hot_count = 2;
    X[0].fine_count = 1;
    X[0].I_count = 0;
    
    X[0].E_count = 2;
    X[0].M_count = 2;
    X[0].S_count = 2;
    
    X[0].active = 1;
   


    X[1].cold_count = 2;
    X[1].hot_count = 1;
    X[1].fine_count = 2;
    X[1].I_count = 1;
    
    X[1].E_count = 2;
    X[1].M_count = 2;
    X[1].S_count = 2;
   
    X[1].active = 1;
   

    X[2].cold_count = 1;
    X[2].hot_count = 2;
    X[2].fine_count = 3;
    X[2].I_count = 0;
    
    X[2].E_count = 4;
    X[2].M_count = 1;
    X[2].S_count = 1;
   
    X[2].active = 1;
    

    X[3].cold_count = 1;
    X[3].hot_count = 2;
    X[3].fine_count = 3;
    X[3].I_count = 0;
    
    X[3].E_count = 4;
    X[3].M_count = 1;
    X[3].S_count = 1;
   
    X[3].active = 0;
   
    
    X[4].cold_count = 1;
    X[4].hot_count = 2;
    X[4].fine_count = 3;
    X[4].I_count = 0;
    
    X[4].E_count = 3;
    X[4].M_count = 0;
    X[4].S_count = 3;
   
    X[4].active = 1;
    

    
    
    
    X[5].cold_count = 1;
    X[5].hot_count = 2;
    X[5].fine_count = 3;
    X[5].I_count = 0;
    
    X[5].E_count = 2;
    X[5].M_count = 1;
    X[5].S_count = 3;
   
    X[5].active = 1;
    





    for (int i =0; i<num_set_per_slice; i++) {
        record a = X[i]; 
        assert( num_set_per_slice == a.fine_count + a.cold_count + a.hot_count + a.I_count); 
    }

    std::sort(X.begin(), X.end(), &CompareRecords);
    //std::stable_sort(X, X+3, &CompareGender);
    //std::stable_sort(X, X+3, &CompareAge);
    //std::stable_sort(X, X+1, &CompareAge);
    
     for (int i =0; i<num_set_per_slice; i++) {
        cout<<X[i].index<<endl; 
    } 
return 0;
}
