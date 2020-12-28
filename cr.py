n = int(input())
a = []
for i in range(n):
    [a.append(i) for i in input().split()]
b = [i.lower() for i in set(a)]
c = set(b)
a = []
stetchic = 0
for i in c:
    for k in range(len(b)):
        if i == b[k]:
            stetchic += 1
    if stetchic > 2:
        a.append(stetchic)
        a.append(i)
    stetchic = 0
for i in range(0,len(a))
print(d)

#s=[[w,0] for w in input().split()]
#dict = {s[i][0]:s.count(s[i]) for i in range(len(s))}
#for i in sorted(dict.items(),key=lambda a:(-a[1],a[0])):
#print(i[1],i[0])