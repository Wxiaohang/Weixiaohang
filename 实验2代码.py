f = open("yq_in.txt")
lines = f.readlines()
list1 = []
list2 = []
for l in lines:
    s = l.split()
    us = s[:]
    list1.append(us)
print(list1)
a = [['浙江省']]
b = [[], ['江西省']]
c = [[], ['广东省']]
d = [[], ['江苏省']]
e = [[], ['湖南省']]
f = [[], ['安徽省']]
g = [[], ['陕西省']]
h = [[], ['河南省']]
k = [[], ['贵州省']]
for i in list1:
    if i[0] == "浙江省":
        a.append(i[1:3])
    if i[0] == "江西省":
        b.append(i[1:3])
    if i[0] == "广东省":
        c.append(i[1:3])
    if i[0] == "江苏省":
        d.append(i[1:3])
    if i[0] == "湖南省":
        e.append(i[1:3])
    if i[0] == "安徽省":
        f.append(i[1:3])
    if i[0] == "陕西省":
        g.append(i[1:3])
    if i[0] == "河南省":
        h.append(i[1:3])
    if i[0] == "贵州省":
        k.append(i[1:3])
list2.extend(a + b + c + d + e + f + g + h + k)
print(list2)
with open("yq_out.txt", "w") as f:
    for i in list2:
        for j in i:
            f.write(j)
            f.write(' ')
        f.write('\n')
    f.close()
