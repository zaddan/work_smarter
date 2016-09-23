#include<iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#define floatingPtWidth 32
#define MANTISA_WIDTH 23
#define bias 127
using namespace std;

unsigned getNumberOfDigits (long unsigned i)
{
    return i > 0 ? (int) log2 ((double) i) + 1 : 1;
}

typedef struct{
    long Exp, Sign, Mantisa; 
    long MantisaWithOne;
}fpType;

void getFPComponents(float number, fpType &num){
 unsigned int* ptr = (unsigned int*)&number;
 num.Sign = *ptr>> 31;
 num.Exp = *ptr& 0x7f800000;
 num.Exp >>= MANTISA_WIDTH;
 num.Mantisa = *ptr& 0x007fffff;
}

float convertFPCompToFP(fpType num){
    float result = 0;
    int expSoFar = num.Exp - bias; //what exp to use at the moment
    int decodedMantisaWithExtraOne = (1 <<MANTISA_WIDTH) + num.Mantisa;//decode mantisa with Extra one
    int mask = 1 << MANTISA_WIDTH;
    int shftRightAmt = MANTISA_WIDTH;
    while(1)  {
        result += ((decodedMantisaWithExtraOne & mask) >>  shftRightAmt)* pow(2, expSoFar );
        mask = mask >> 1; 
        shftRightAmt -= 1;
        expSoFar -=1;
        if (mask == 0) {
            break;
        }
    }

    if (num.Sign) {
        result = -1*result;
    }
    return result;
}

void normalizeMul(fpType &resultNum){ 
    int numOfDig = getNumberOfDigits (resultNum.Mantisa);
    if (numOfDig > MANTISA_WIDTH + 1) {
        resultNum.Mantisa = resultNum.Mantisa >> (numOfDig - (MANTISA_WIDTH + 1));
        resultNum.Exp= resultNum.Exp + (numOfDig - (2*MANTISA_WIDTH + 1));
    }else{
        ; //do nothing
    }
}

void normalizeAdd(fpType &resultNum){ 
    int numOfDig = getNumberOfDigits (resultNum.Mantisa);
    if (numOfDig > MANTISA_WIDTH + 1) {
        resultNum.Mantisa = resultNum.Mantisa >> (numOfDig - (MANTISA_WIDTH + 1));
        resultNum.Exp= resultNum.Exp + (numOfDig - (MANTISA_WIDTH + 1));
    }else{
        ; //do nothing
    }
}
float Addition(float number1, float number2, int numApxBit) {
    fpType num1;
    fpType num2;
    float apxResult; 
    fpType result; 
    fpType bigNum;
    fpType smallNum;
    int signMultiplicand; 
    
    getFPComponents(number1, num1); //get the fp componenets
    getFPComponents(number2, num2); //get the fp components
    num1.MantisaWithOne = (1 <<MANTISA_WIDTH) + num1.Mantisa;//injaect mantisa with Extra one
    num2.MantisaWithOne =   (1 <<MANTISA_WIDTH) + num2.Mantisa;//injaect mantisa with Extra one
     
    if (num1.Exp  < num2.Exp) { //decide on the small and big number
      bigNum = num2;
      smallNum = num1;
    }  else {
      bigNum = num1;
      smallNum = num2;
    }
    
    smallNum.MantisaWithOne = smallNum.MantisaWithOne >> (bigNum.Exp - smallNum.Exp); // align the small num
    if (bigNum.Sign == smallNum.Sign) { //same sign
        result.Mantisa = (bigNum.MantisaWithOne +  smallNum.MantisaWithOne);
        result.Exp = bigNum.Exp;
        result.Sign = bigNum.Sign;
        normalizeAdd(result);
        result.Mantisa =  (result.Mantisa >> numApxBit) << numApxBit; //truncate mantisa
        result.Mantisa =  result.Mantisa - (1<<MANTISA_WIDTH); 
        apxResult = convertFPCompToFP(result);
    }else{ //diff sign
            result.Mantisa = (bigNum.MantisaWithOne - smallNum.MantisaWithOne);
            result.Exp = bigNum.Exp;
            result.Sign = bigNum.Sign; 
            normalizeAdd(result);
            result.Mantisa =  (result.Mantisa >> numApxBit) << numApxBit; //truncate mantisa
            result.Mantisa =  result.Mantisa - (1<<MANTISA_WIDTH); 
            apxResult = convertFPCompToFP(result);
    }

    return apxResult; 
}

float Multiplication(float number1, float number2, int numApxBit) {
    fpType num1;
    fpType num2;
    float apxResult; 
    fpType result; 
    
    getFPComponents(number1, num1); //get the fp componenets
    getFPComponents(number2, num2); //get the fp components
    num1.MantisaWithOne = (1 <<MANTISA_WIDTH) + num1.Mantisa;//injaect mantisa with Extra one
    num2.MantisaWithOne =   (1 <<MANTISA_WIDTH) + num2.Mantisa;//injaect mantisa with Extra one
    result.Mantisa = num1.MantisaWithOne *  num2.MantisaWithOne;
    result.Exp = num1.Exp + num2.Exp - bias;
    result.Sign = (num1.Sign + num2.Sign)%2;
    normalizeMul(result);
    result.Mantisa =  (result.Mantisa >> numApxBit) << numApxBit; //truncate mantisa
    result.Mantisa =  result.Mantisa - (1<<MANTISA_WIDTH); 
    apxResult = convertFPCompToFP(result);
    return apxResult; 
}






int main() {

float number1 = -1000000.340000005;
float number2 = 20.500203;
float number3;
number3 = Addition(number1, number2,0);
//number3 = Multiplication(number1, number2,20);
//float number4 = number1*number2;

float number4 = number1 + number2;
cout << "number3: " << number3 <<endl;
cout << "number4: " << number4 <<endl;
}
