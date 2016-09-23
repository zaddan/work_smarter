x = symbols('x[0]') #define a symbol first
a = 4*2*pow(x,2) # define an equation using the symbol
b = 10*x 
c = a+b
print c  
print c.subs(x,2) #subs can be used for both substituion of variables and also
# numbers for variabels

