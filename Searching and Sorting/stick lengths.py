'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=list(map(int,input().split()))
l=sorted(arr)
m=(n-1)//2
c=0
for i in range(n):
    d=abs(l[i]-l[m])
    c=c+d
print(c)