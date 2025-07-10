#1 Arithmetic  operators

a=20
b=10
print("Addition (+)",a+b) #Addition(+): 30
print("Substraction (-)",a-b) #Substraction(-) : 10
print("Multiplicatin (*)",a*b) #Multiplication(*) : 200
print("Division (/)",a/b) #Division(/) : 2.0
print("Floor division (//)",a//b) #floor division(//) : 2
print("Modulus(/)",a%b) #Modulus(/) : 0
print("Exponentation (**)",a**b) #exponentation(**) : 102400000000


#2 Comparision operators
print("Equal to (==)",a==b) #Equal to(==): False
print("Not equal to (!=)",a!=b) #Not equal to(!=) : True
print("Greater than(>)",a>b) #Greater than(>) : True
print("Less than (<)",a<b) #Less than(<) : False
print("Greater than  or Equal to(>=)",a>=b) #Greater than  or Equal to(>=) : True
print("Less than or Equal to (<=)",a<=b) #Less than or Equal to (<=) : False


#3 Assignment operators
print("Assign(=):",a) #Assign(=) :20
a=b
print("Add & Assign(+=):",a) #Add & Assign(+=) :10
a+=b 
print("Subtract & Assign(-=)",a) #Subtract & Assign(-=) : 20
a-=b
print("Multiply & Assign(*=):",a) #Multiply & Assign(*=) : 10
a*=b
print("Divide & Assign(/=):",a) #Divide & Assign(/=) : 100
a/=b 
print("Floor Divide & Assign(//=)",a) #Floor Divide & Assign(//=) :10.0
a//=b
print("Modulus & Assign(%=):",a) #Modulus & Assign(%=) : 1.0
a%=b 
print("Exponentiate & Assign(**=):",a) #Exponentiate & Assign(**=) : 1.0
a**=b

#4.Logical Operators (Using Logic Gates)
print("AND operator:",a>b and b>a) #AND operator: False
print("OR operator:",a<b or b<a) #OR operator: True
print("NOT operator:",not a>b) #NOT operator: False


#5.Membership Operators
a = [1,2,3]
print("In operator:",1 in a) #In operator: True
print("Not In operator:",5 not in a) #Not In operator: True


#6.Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Is operator:",a is b) #In operator: True
print("Is Not operator:",a is not c) #Not In operator: True


#bitwise operators

print("and operator:",a&b)
print("or operator:",a|b)            
print("XOR operator:",a^b)
print("Not operator:",~b)
print("left shift operator:",a<<b)
print("right shift operator:",a>>b)
