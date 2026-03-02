l=[]
m=[]
sum1=0
sum2=100000000
name2=''
name1=''
x=int(input())
for a in range(0,x):
    y=int(input("marks"))
    l.append(y)
for a in range((x-1),-1,-1):
    m.append(l[a])
print(m)
print(l)






