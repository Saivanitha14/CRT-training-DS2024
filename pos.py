list2=[]
pos=0
neg=0
for i in range(0,5):
    list2[i]=int(input())
for i in range(0,5):
    if list2[i]>=0:
        pos=pos+list2[i]
    else:
        neg=neg+list2[i]

print(pos,neg)
print(pos+neg)
