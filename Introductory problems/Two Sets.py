'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
n=int(input())
l=[]
l1=[]
l2=[]
for i in range(1,n+1):
    l.append(i)
value=(n*(n+1))//2
def ans(arr):
    for i in range(len(arr)//4):
        l1.append(arr[i])
        l1.append(arr[len(arr)-1-i])
    print("YES")
    print(len(l1))
    print(" ".join(map(str,l1)))
    l2=list(set(l)-set(l1))
    print(len(l2))
    print(" ".join(map(str,l2)))
if value%2!=0:
    print("NO SOLUTION")
elif n%4==0:
    ans(l)
elif n%4==3:
    l1.append(l[0])
    l1.append(l[1])
    ans(l[3:n])
else:
    print("NO")
    
        
    
