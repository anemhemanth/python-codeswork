n=int(input("enter the size:"))

""" for row in range(n):
    for col in range(n):
        print('*', end=' ')
    print() """


""" for row in range(n):
    for col in range(n + 1):
        print('*', end=' ')
    print() """



""" 
for row in range(n):
    print(' '*row,end='')
    print(""(n-row),end='')
    print()
    

for row in range(n):
    if row<=n//2:
        print(""(row+1),end=' ')
    else:
        print(""(n-row),end=' ')
    print() """
    


""" for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()



for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
 """


""" for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or (col==0 and row<n//2) or col==n-1 and row>=n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    

for row in range(n):
    for col in range(n):
        if row==0 or row==n//2 or col==0 or col==n-2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    

for row in range(n):
    for col in range(n):
        if col==row or col==n-row:
            print("*",end='')
        else:
            print(" ",end='')
    print() """



