'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
nm=list(map(int,input().split(" ")))
price=list(map(int,input().split(" ")))
maxp=list(map(int,input().split(" ")))
n=nm[0]
m=nm[1]
l1=sorted(price)
for i in range(len(maxp)):
    j =0
    flag=False
    while(j<len(l1) and maxp[i]>=l1[j]):
        j+=1
        flag=True
    if flag:
        print(l1[j-1])
        l1.remove(l1[j-1])
    else:
        print(-1)
    

