
a,b=map(int,raw_input().split())
for i in range(a,b+1):
    if(i%2!=0):
        print i,
        i +=1
