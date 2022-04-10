'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
time=[]
for i in range(n):
    x,y=map(int,input().split())
    time.append([x,y])
l=sorted(time,key=lambda x:x[1])
c=0
ans=0
for start,end in l:
    if start>=c:
        ans+=1
        c=end
print(ans)

