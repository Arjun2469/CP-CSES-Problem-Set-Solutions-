'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
s=0
e=n-1
m=s+e//2
if n%2==0:
    l[s]=2
    l[e]=n-1
    l[m]=n
else:
    l[s]=2
    l[e]=n
    l[m]=1
j=1
while(j<m):
    l[j]=l[s]+2*j
    j+=1
k=n-2
a=1
while(k>m):
    l[k]=l[e]-2*(a)
    k-=1
    a+=1
if n==1:
    print(1)
elif n>1 and n<4:
    print("NO SOLUTION")
else:
    print(" ".join(map(str,l)))