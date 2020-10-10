z=input().split(" ")
(n,k)=(int(z[0]),int(z[1]))
b=[]
a=[]
c=[]
d=[]
e=[]
f=[]
for l in range(n):
        x=input().split(" ")
        a.append(x)
for i in range(k):
    y=input().split(" ")
    b.append(y)
for j in range(n):
    c.append(a[j][0])
    d.append(a[j][1])
    e.append(a[j][2])
ma1=max(c)
f.append(ma1)
ma2=max(d)
f.append(ma2)
f.append(ma3)
if(f==b[0]):
    print("YES")
else:
    print("NO")
if(f==b[1]):
    print("YES")
else:
    print("NO")









