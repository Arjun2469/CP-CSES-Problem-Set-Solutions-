'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=input()
def per(s):
    if len(s)==1:
        return [s]
    perm=per(s[1:])
    char=s[0]
    l=[]
    for p in perm:
        for i in range(len(p)+1):
            l.append(p[:i]+char+p[i:])
    return l
result=sorted(list(set(per(n))))
print(len(result))
for j in result:
    print(j)


        
        