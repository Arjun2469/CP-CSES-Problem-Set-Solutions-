'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
l=[]
 
for i in range(n):
    l.append(list(map(int,input().split(" "))))
for j in range(n):
    m=min(l[j][0],l[j][1])
    a=max(l[j][0],l[j][1])
    if (l[j][0]+l[j][1])%3==0 and m>=a//2:
        print("YES")
    else:
        print("NO")