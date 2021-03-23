import string

test1 = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
test2 = "How quickly daft jumping zebras vex"
test3 = "Cwm fjord bank glyphs vext quiz"
test4 = "Pack my box with five dozen liquor jugs"
tests = [test1, test2, test3, test4]


def is_pangram(s):
    # return true if all letters from a-z are represented in s and false otherwise
    letters_represented = [x for x in string.ascii_lowercase if x in s.lower()]
    return string.ascii_lowercase == ''.join(letters_represented)

# TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for test in tests:
    print(is_pangram(test))


def generate_all_possible_matches(k):
    # two of us play a game up to a score of k
    # return all possible scores for the game
    # (k+1)^2 possible matches print all of them
    k += 1
    matches = []

    for i in range(k):
        for j in range(k):
           matches.append(str(i) + ":" + str(j))
    
    return matches

# TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for k in range(100):
    print(len(generate_all_possible_matches(k)) == (k+1**2)
    

source_array1 = [5, 3, 1, 8, 0]
source_array2 = [5, 8, 6, 3, 4] 

arrays = [source_array1, source_array2]


def sort_array(source_array):
    # sort the odd numbers in ascending order while 
    # leaving the even numbers at their original positions.
    numbers = [x for x in source_array if x%2 !=0]
    numbers.sort()

    output = []

    i = 0
    for number in source_array:
        if number % 2 == 0:
            output.append(number)
        else:
            output.append(numbers[i])
            i += 1
    return output
            
# TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
for source in arrays:
    print(sort_array(source))