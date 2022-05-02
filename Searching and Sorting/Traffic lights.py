'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

i1=list(map(int,input().split()))
n=i1[0]
l=list(map(int,input().split()))
arr=[0]*(n+1)
ans=[]
for i in l:
    d=0
    c=0
    arr[i]=1
    for j in range(n+1):
        if arr[j]==0:
            continue
        else:
            d=max(j,n-j)
        #if d<c:
            #d=c
    ans.append(d)
print(ans)