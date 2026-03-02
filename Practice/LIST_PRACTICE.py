#array rotation
LIST1=[1,2,3,4,5]
n=int(input("enter the no of times rotaion is performed"))
LIST2=LIST1[:]
LIST3=[]
k=len(LIST1)
for i in range(0,n):
    LIST3=[]
    LIST3.append(LIST2[k-1])
    LIST3+=LIST2[:k-1]
    LIST2=LIST3[:]
    print(LIST3)
    
#