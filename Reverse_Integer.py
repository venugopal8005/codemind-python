import math
n=int(input())
s=0
a=abs(n)
while(a!=0):
    r=a%10
    s=s*10+r
    a=a//10
if(n>0):
    print(s)
else:
    print(-1*s)