p,m=map(int,input().split())
n=[]
t=[]
gcd=1
for i in range(2,p+1):
    if(p%i==0):
        while(p%i==0):
            n.append(i)
            p=p//i
for j in range(2,m+1):
    if(m%j==0):
        while(m%j==0):
            t.append(j)
            m=m//j
print(n)
print(t)
for y in n:
    for z in t:
        if (y==z):
            gcd=gcd*y
            t.remove(y)
            n.remove(y)
print(n)
print(t)
print(gcd)
