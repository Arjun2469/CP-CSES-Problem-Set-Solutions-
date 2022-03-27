'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
a,b,c=1,2,3
def toh(n,a,b,c):
    if n>0:
        toh(n-1,a,c,b)
        print(a,"",c)
        toh(n-1,b,a,c)
print(2**n-1)
toh(n,a,b,c)
