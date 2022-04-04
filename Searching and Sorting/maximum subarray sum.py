'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import sys
n=int(input())
arr=list(map(int,input().split(" ")))
max1=-sys.maxsize-1
s=0
for i in range(n):
    s=s+arr[i]
    if s<arr[i]:
        s=arr[i]
    if max1<s:
        max1=s
print(max1)

