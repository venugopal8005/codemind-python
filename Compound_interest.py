p,r,t=map(int,input().split())
a=p*((1+(r/100))**t)
c=a
print(format(c,".2f"))