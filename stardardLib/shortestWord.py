def find_short(s):
    lengths = [len(x) for x in s.split()]
    return min(lengths)

s = "bitcoin take over the world maybe who knows perhaps"
s.split()


def accum(s):
    new = [(x * i).capitalize() for x, i in enumerate(s, start=1)]
    return '-'.join(new)
 


s = "ZpglnRxqenU"
accum(s)



[word.upper() for word in new[1:]]

new
for i in range(len(new)):
    print(len(new[i]))
    
'-'.join(new)


def xo(s):
    n_x = len([x for x in s if x == "x"])
    n_o = len([i for i in s if i == "o"])

    if n_x == n_o:
        return 'true'
    else:
        return 'false'
    
    
s = "XxXOoO"


n_x = len([x for x in s if x in "Xx"])
n_o = len([i for i in s if i in "Oo"])
     
n_x
n_o


def to_jaden_case(string):

string = "How can mirrors be real if our eyes aren't real"

string.title()



string

string.upper()


[x[0].capitalize() for x, i in enumerate(string, start=1)]

string = "How can mirrors be real if our eyes aren't real"

[x for x in string]


string = string.split(' ')


l = []
for i in range(len(string)):
     l.append(string[i].capitalize())
    

def to_jaden_case(string):
    string = string.split(" ")
    l = []
    for i in range(len(string)):
         l.append(string[i].capitalize())
    
    return ' '.join(l)

string = "How can mirrors be real if our eyes aren't real"
to_jaden_case(string)


def filter_list(l):
    listlist = [str(x) for x in l]
    new = []
    for i in range(len(listlist)):
        yo = listlist[i]
        if yo.isdigit():
            if int(yo) not in new:
                yo = int(yo)
                new.append(yo)
            
    return new

l = [1, 2, 1, 123, 123]

filter_list(l)


def is_isogram(string):
    liststring = [x.lower() for x in string]
    if len(string) == len(set(liststring)):
        return True
    else:
        return False

def sum_two_smallest_numbers(numbers):
    nums = numbers
    minimum = min(nums)
    first = nums.index(minimum)
    del nums[first]
    second_min = min(nums)
    return minimum + second_min    



def find_it(seq):
    seqset = set(seq)
    seqset = list(seqset)

    for i in range(len(seqset)):
        n = seq.count(seqset[i])
        if n % 2 != 0:
            return seqset[i]
    
seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
find_it(seq)
