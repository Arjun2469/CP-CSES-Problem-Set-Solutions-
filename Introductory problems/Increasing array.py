'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=list(map(int,input().split(" ")))
c=0
for i in range(n-1):
    if arr[i]>arr[i+1]:
        d=arr[i]-arr[i+1]
        arr[i+1]=arr[i]
        c+=d
print(c)
