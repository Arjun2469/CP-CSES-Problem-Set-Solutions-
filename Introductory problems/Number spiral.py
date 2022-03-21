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
    m=max(l[j][0],l[j][1])
    f=m*(m-1)+1+((-1)**m)*(l[j][0]-l[j][1])
    print(f)
    
