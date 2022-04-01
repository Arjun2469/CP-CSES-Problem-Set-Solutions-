'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
n=l1[0]
x=l1[1]
ans=[]
l2=sorted(l2)
w=l2[::-1]
l=0
r=n-1
while(l<=r):
    if w[l]+w[r]<=x:
        ans.append([w[l],w[r]])
        l+=1
        r-=1
    else:
        ans.append([w[l]])
        l+=1
print(len(ans))

        
    