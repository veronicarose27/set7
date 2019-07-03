import math
o,p=map(int, input().split())
r=o*p
l=math.sqrt(r)
if(l==int(l)):
    print('yes')
else:
    print('no')
