'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input())
arr=list(map(int,input().split()))
j,k=0,set()
ans=0
for i in range(n):
    while arr[i] in k:
        k.remove(arr[j])
        j+=1
    k.add(arr[i])
    ans=max(ans,len(k))
print(ans)