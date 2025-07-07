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

#Replace & Modify Methods

print(text1.replace("h","i"))

print(text1.translate(str.maketrans("e","@")))

print(text1.maketrans("hello","@&%*"))


#Splitting & Joining Methods

print(text1.split(" "))#Splits the string into a list by sep

print(text1.rsplit(" "))# Splits from the right side.


print(text1.splitlines(" "))#Splits at line breaks ( ).


result=' '.join(text1)# Joins elements with a separator.
print(result)

text2="hello-world"#Splits into a 3-part tuple at first sep.
print(text2.partition("-"))

print(text2.rpartition("-"))# Splits into a3-part tuple at last sep.

#Whitespace & Trimming Methods

print("  hello ".strip()) #Removes leading and trailing characters (default: spaces).

print("----hello".lstrip("-"))#Removes leading characters.

print("hello----".rstrip("-")) #Removes trailing characters.