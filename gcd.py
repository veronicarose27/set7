p,m=map(int,input().split())
n=[]
t=[]
gcd=1
for i in range(1,p+1):
    if(p%i==0):
        n.append(i)
for j in range(1,m+1):
    if(m%j==0):
        t.append(j)
for y in n:
    if y in t:
        gcd=gcd*y
print(gcd)
