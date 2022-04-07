'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=[]
dep=[]
for i in range(n):
    x,y=input().split()
    arr.append(x)
    dep.append(y)
arr.sort()
dep.sort()
c=0
cur=0
i,j=0,0
while(i<n and j<n):
    if arr[i]<dep[j]:
        cur+=1
        i+=1
    else:
        cur-=1
        j+=1
    if c<cur:
        c=cur
print(c)
