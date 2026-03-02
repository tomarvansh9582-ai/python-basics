s=str(input())
k=""
for a in range(0,len(s)):
    if a==0:
        m=s[0].upper()
        k=k+m
    else:
        if s[a-1]==" ":
          m=s[a].upper()
          k=k+m
        else:
          k=k+s[a]
print(k)
