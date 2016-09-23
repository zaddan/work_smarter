#include <string.h>
#include <stdio.h>
#include <sstream>    
#include <iostream>
using namespace std;
/* Counting the number of decimals
 *
 * 1. Use Scientific Notation format
 * 2. Convert it to a string
 * 3. Tokenize it on the exp sign, discard the base part
 * 4. convert the second token back to number
*/
int number_of_decimals(float value){
   ostringstream tmpString; 
   tmpString << value;
   string valueConvertedToString = tmpString.str(); 
    
   string decimalPart = valueConvertedToString.substr(valueConvertedToString.find(".")+1);
   return decimalPart.length() ;
}

int main(){
   float real = 35.001;
  
   cout << number_of_decimals(real);
}
