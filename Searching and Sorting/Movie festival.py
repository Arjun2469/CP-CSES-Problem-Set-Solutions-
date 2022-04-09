'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
start=[]
for i in range(n):
    x,y=map(int,input().split())
    start.append([x,y])
l=sorted(start,key=lambda x:x[1])
c=1
j=1
for i in range(1,n):
    if l[i][0]>=l[j-1][1]:
        c+=1
        j+=1
print(c)


