#if and else
items=['car','bike','scooty','watch']
print("welcome to flipcart".center(80,'-'))
searchitem=input("enter the item: ").lower()

if searchitem in items:
    print("found ")
else:
    print("not found")


#weekend budget
amount=int(input("Enter the amount you can spend for weekend:"))
if amount>20000:
    print("triop to goa")
elif amount>15000:
    print("Go for shopping")
elif amount>10000:
    print("Clubing")    
elif amount>15000:
    print("cafe")    
elif amount>2000:
    print("buffet")
elif amount>500:
    print("movie") 
else:
    print("save the money and sleep")  

#3
num=int(input("enter the number:"))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")

#4
