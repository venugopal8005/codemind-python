a,b=map(int,input().split())
if(b==a+1 or a==b+1):
    print("Yes")
elif((a==1 and b%10==0) or (b==1 and a%10==0)):
    print("Yes")
else:
    print("No")