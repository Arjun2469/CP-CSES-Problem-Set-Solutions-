'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=input()
c=0
max1=0
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c+=1
        if c>max1:
            max1=c
    else:
        c=0
print(max1+1)