'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=list(map(int,input().split()))
max1=arr[0]
c=1
for i in range(1,n):
    if arr[i]>=max1:
        max1=arr[i]
        c+=1
print(c)
    