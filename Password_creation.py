def newPassword(a,b):
    d=""
    a1=len(a)
    if(len(b)<a1):
        a1=len(b)
    for i in range(0,a1):
        d=d+a[i]
        d=d+b[i]
    c=abs(len(a)-len(b))
    if(len(a)>len(b)):
        d=d+a[-c:]
    else:
        d=d+b[-c:]
    return d

a = input()
b=input()
print(newPassword(a,b))
