n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in range(0,n-1,2):
    l[i],l[i+1]=l[i+1],l[i]
for i in l:
    print(i,end=' ')