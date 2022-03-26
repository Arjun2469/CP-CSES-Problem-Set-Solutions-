'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
b=2**n
def binary(a):
    bn=bin(a).replace("0b","")
    if len(bn)!=n:
        bn="0"*(n-len(bn))+bn
    return bn
def gray(num):
    ans=num[0]
    for j in range(n-1):
        ans+=str(int(num[j])^int(num[j+1]))
    print(ans)
for i in range(b):
    gray(binary(i))
    
        
        

    

    
