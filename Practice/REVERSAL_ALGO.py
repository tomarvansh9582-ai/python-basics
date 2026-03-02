#reversal algo in list\array
list1=[1,2,3,4,5]
d=int(input("enter the rotation"))
list1[:d]=reversed(list1[:d])
list1[d:]=reversed(list1[d:])
list1.reverse()
print("reversed list is:",list1)