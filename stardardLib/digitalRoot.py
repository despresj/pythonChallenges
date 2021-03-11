def digital_root(n):
    digRoot = n
    while digRoot >= 10:
        digitsInN = [int(str(x)) for x in str(digRoot)]
        digRoot = sum(digitsInN)
    return digRoot

digital_root(923542)

# ([1,2,2], [1]), [2,2],
a, b = [1,2], [1]
def array_diff(a, b):
    return [x for x in a if x not in b]
array_diff(a, b)



# party outlier
([160, 3, 1719, 19, 11, 13, -21]), 160)
([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
([2, 4, 6, 8, 10, 3]), 3)

def find_outlier(integers):
    nums = [x for x in integers if x % 2 == 0]
    if len(nums) == 1:
        return nums[0]
    else:
        odd = [x for x in integers if x % 2 != 0]
        return odd[0]


integers = [160, 3, 1719, 19, 11, 13, -21]
find_outlier(integers)
integers = [2, 4, 0, 100, 4, 11, 2602, 36]
find_outlier(integers)
integers = [2, 4, 6, 8, 10, 3]
find_outlier(integers)





# "din"),"(((")
# "recede"),"()()()")
# "Success"),")())())","should ignore case")
# "(( @"),"))((")

def duplicate_encode(word):
    word = [x.lower() for x in word] 

    all_freq = {}

    for i in word: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1

    new_str = []
    for i in word:
        if all_freq[i] == 1:
            new_str.append("(")
        else:
            new_str.append(")")
            
    return ''.join(new_str)

duplicate_encode("Success")

def persistence(n):
        new = n
        iters = 0
        while new > 9:
            iters += 1
            numlist = [int(x) for x in str(new)]
            new = 1
            for number in numlist:
                new *= number
        return iters

persistence(n = 25)


walk = ['n','n','n','s','n','s','n','s','n','s']
walk = ['n','s','n','s','n','s','n','s','n','s']

def is_valid_walk(walk):
    # make dict
    keys = 'n', 's', 'e', 'w'
    all_freq = {key: 0 for key in keys}
    
    # count items
    for i, x in enumerate(walk): 
            all_freq[x] += 1      
            
    # Conditions
    northEqualSouth = all_freq['n'] == all_freq['s']
    eastEqualWest = all_freq['e'] == all_freq['w']
    tenMin = len(walk) == 10

    if tenMin and northEqualSouth and eastEqualWest:
        return True
    else:
        return False

is_valid_walk(walk)
