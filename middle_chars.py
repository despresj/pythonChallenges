def get_middle(s):
    if len(s) % 2 == 0:
        second = int(len(s) / 2)
        first = second - 1
        index = [first, second]
        middle = [(x, y) for (x, y) in enumerate(s) if x in index]
        return middle[0][1] + middle[1][1]  
    else:
        index = len(s) //2 
        middle = [(x, y) for (x, y) in enumerate(s) if x == index]
        return middle[0][1]








get_middle("test")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")