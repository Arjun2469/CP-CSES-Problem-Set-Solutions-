'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=list(map(int,input().split(" ")))
a=n*(n+1)//2
ans=a-sum(arr)
print(ans)