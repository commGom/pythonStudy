import sys
read=sys.stdin.readline

N=int(read())

sequence_list=list(map(int,read().split()))

# print(sequence_list)

d=[1]*N

for i in range(N):
    for k in range(i):
        if sequence_list[i]>sequence_list[k]:
            d[i]=max(d[i],d[k]+1)
            # print(d)

max_val=max(d)     
val_list=[0]*(max_val+1)
val=max_val
for i in range(N-1,-1,-1):
         if val==d[i]:
            val_list[val]=sequence_list[i]
            val-=1       
            
print(max_val)
for i in range(1,len(val_list)):
    print(val_list[i],end=" ")