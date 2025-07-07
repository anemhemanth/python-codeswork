# list with elements
l=list([1,4,5])
print(l)
l=list([1,3,4,"lewis",9.0,3+9j])
print(l)
l.append(True)
print(l)

#list with nested lists
l=[[1,4,5],["leclarc",'kimi'],[1.7,7.9],[True,False]]
print(l)
 
# list using indexin positive and negative
a=["hamilton",'londo',"oscar"]
print(a[0])
print(a[2])
print(a[-3])
print(a[::-1])
 
b=[30,80,45,78,90]
print(b[:3]) 
print(b[-1:])
print(b[-3:-1])
print(b[-2:-1])
   
# changing elements
n=[90,88,77,55]
print(n[2])
n[3]=99
print(n)

# adding elements
n=[90,88,77,55]
n.append(900)
print(n)
n.insert(1,20)
print(n)
n.extend([11,33,44])
print(n)
    
#removing of elements
p=[10, 15, 20, 100, 40, 50, 60, 70, 80]
p.remove(100)
print(p)  
p.pop()
print(p)
p.pop(0)
print(p)
del p[3]
print(p)  
p.clear()
print(p)
#fghjhgkhjkiij
l=[1,4,5,9,7,9,7]
print(l.index(5))
print(l.count(7))
l.sort()
print(l)
l.reverse()
print(l)

#copying alist
l = [1, 2, 3,90,70,60,0,100000]
l.copy()
print(any(l))
print(all(l))
print(len(l))
print(max(l))
print(min(l))
