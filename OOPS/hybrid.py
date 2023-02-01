# highest number formed from the number of digits inputed is a hybrdi number or not
n = int(input())
a = 10**(n) - 1
for i in range(a,0,-1):
    temp = False
    temp2= False
    flag = 0
    t = str(i)
    l = t[::-1]
    if t == l:
        temp = True
    for j in range(2,i):
        if i % j == 0:
            flag += 1
    if flag == 0:
        temp2 = True
    if temp and temp2 :
        print(i)
        break

        
        
    # temp = 0
    # d = 0
    # result =