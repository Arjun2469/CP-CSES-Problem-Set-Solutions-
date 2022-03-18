'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
print(n,end=" ")
while(n!=1):
    if n%2==0:
        n=n//2
        print(n,end=" ")
    else:
        n=n*3+1
        print(n,end=" ")
