n=input()
s=''
c=0
for i in n:
    if i in 'aeiou' and c==0:
        s+='V'
    else:
        s+='C'
for i in range(len(s)-1):
    if(s[i]!=s[i+1]):
        print(s[i],end='')
print(s[len(s)-1])
        
    
