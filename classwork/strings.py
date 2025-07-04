 #operations of strings
n1="lewis"
n2="hamilton"
print("concatenation of strings:",n1+n2)
print("lewis" *3)
print(n1[4])
print(n2[2])
print(n1[0:4])
print(n2[:2])
print('lewis' in n1)
print("python" not in n2)

#built in string functions
k="python programming"
print(len(k))
print(max('sonny'))
print(min("sonny"))
print(sorted('python'))
print(chr(97))
print(ord('s'))

#python string methods 
# case conversion methods
x="need to race"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
y='PyThOn'
print(y.swapcase())

# Alignment and formatting methods
y='charles to drive'
print(y.center(30,"*"))
print(y.center(20,"_"))
print(y.rjust(20,'_'))
print(y.ljust(20,"_"))
w="899"
print(w.zfill(5))


#search and find methods
u="kiwilewislecrec"
print(u.find("kiwi"))
print(u.find('s'))
print(u.count('c'))
print(u.index('w'))
print(u.rfind("i"))
