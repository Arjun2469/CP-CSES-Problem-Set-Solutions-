'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

arr1=list(map(int,input().split(" ")))
arr2=sorted(list(map(int,input().split(" "))))
arr3=sorted(list(map(int,input().split(" "))))
n=arr1[0]
m=arr1[1]
k=arr1[2]
i,j=0,0
ans=0
while(i<n and j<m):
    if abs(arr2[i]-arr3[j])<=k:
        i+=1
        j+=1
        ans+=1
    else:
        if arr2[i]-arr3[j]>k:
            j+=1
        else:
            i+=1
print(ans)

    
