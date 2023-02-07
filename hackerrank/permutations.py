from itertools import permutations
l2 = []
s = input()
l = s.split(" ")

l1 =list(permutations(l[0],int(l[1])))
for i in l1:
    p = ""
    for j in i:
        p +=j
    l2.append(p)
print(l2)
l2.sort()
for i in l2:
    print(i)