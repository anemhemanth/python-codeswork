# output formatting
a='senna'
print(a)
print(a[::-1])

name="senna"
school="bmw"
Score=70
print("Name:" , name, "School:", school)
print('2024','08','09',sep="-")
print(name,end=" ")
print(school)
print("name \n school")
print("name \t school")
print("name: %s | school: %s | score: %d " % (name, school, Score))
print(f"name:{name} | score:{Score} | School:{school}")