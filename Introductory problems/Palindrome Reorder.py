'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

s=input()
l=list(set(s))
l1=[]
l2=[]
for i in l:
    if s.count(i)%2==0:
        l1+=s.count(i)*[i]
    else:
        l2+=s.count(i)*[i]
l1.sort()
l2.sort()
ans1="".join(l1[::2])
ans2="".join(l2)
ans=ans1+ans2+ans1[::-1]
if ans==ans[::-1]:
    print(ans)
else:
    print("NO SOLUTION")
