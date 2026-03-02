f=open('a.txt','w')
ch=str(input("eneter your string"))
f.write(ch)
f.close()
f=open('a.txt','w')
print(f.read())
f.close()
f=open('a.txt','r')
k='y'
while k=='Y' or k=='y':
    
