b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

def stock_list(listOfArt, listOfCat):
    b,c = listOfArt, listOfCat
    for i in range(len(c)):
        j, total = 0, 0
        new = c
        for j in range(len(b)):
            if  c[i] == b[j][0]:
                total += int(b[j].split()[1])
        new[i] =  new[i] + ' : ' + str(total)
    return new


stock_list(b, c)  

    
(A : 20) - (B : 114) - (C : 50) - (W : 0)