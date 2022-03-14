a = input().split()
mi = a.count(a[0])
li = []
c = ''
for i in range(len(a)):
    if a.count(a[i]) > mi:
        mi = a.count(a[i])
        c = a[i]
if mi == 1:
    a.sort()
    print(a[0])
else:
    li.append(c)
    a.remove(c)
    mi = a.count(a[0])
    for i in range(len(a)):
        if a.count(a[i]) > mi:
            mi = a.count(a[i])
            c = a[i]
    li.append(c)
    li.sort()
    print(li[0])
