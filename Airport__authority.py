n=int(input())
s=[]
c=0
for i in range(n+1):
    m=int(input())
    s.append(m)
for i in range(len(s)-1):
    if(s[i]>s[len(s)-1]):
        c+=2
    else:
        c+=1
print(c)