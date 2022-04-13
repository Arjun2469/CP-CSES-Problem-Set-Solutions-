'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=list(map(int,input().split()))
l=sorted(arr)
c=0
for i in range(n):
    if (c+1)<l[i]:
        break
    c+=l[i]
print(c+1)

        
        
        

