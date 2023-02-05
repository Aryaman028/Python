if __name__ == '__main__':
    l1=[] 
    
    for i in range(int(input())):
        l=[]
        name = input()
        score = float(input())
        l.append(name)
        l.append(score)
        l1.append(l)
        second_lowest = 0
        l1 = sorted(l1,key = lambda x :(x[1],x[0]))
        for i in range(0, len(l1)):
            if l1[i][1] < l1[i+1][1]:
                second_lowest = l1[i+1][1]
                break
        l1.sort()
        for i in range(len(l1)):
            if l1[i][1] == second_lowest:
                print(l1[i][0])       
        


    

    # min = l1[0][1]


    

    # for i in range(len(l1)):
    #     if  l1[i][1] < min:
    #         min = l1[i][1]
    #         index = i
    # l1.pop(i)
    # l1.sort()
    # for i in range(len(l1)):
    #     print(l1[i][0])