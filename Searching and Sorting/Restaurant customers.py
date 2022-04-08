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
    arr.append(int(x))
    dep.append(int(y))
arr.sort()
dep.sort()
max1=0
ans=0
i,j=0,0
while(i<n and j<n):
    if arr[i]<dep[j]:
        ans+=1
        i+=1
    else:
        ans-=1
        j+=1
    if max1<ans:
        max1=ans
print(max1)
