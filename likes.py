def likes(names):
    if condition1:
    print('no one likes this')
elif len(names) == 1:
    likes = names[0] + ' likes this'
    print(likes)
elif len(names) == 2:
    likes = names[0] + ' and ' + names[1] + ' likes this'
    print(likes)
elif len(names) == 3:
    likes = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    print(likes)
elif len(names) > 3:
    likes = names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
    print(likes)
    



names = []
names = ['Peter']
names = ['Jacob', 'Alex']
names = ['Max', 'John', 'Mark']
names = ['Alex', 'Jacob', 'Mark', 'Max']
condition1 = names == []



          
          


'''
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
'''


def create_phone_number(n):
    def collapse_numbers(nums):
        return ''.join([str(x) for x in nums])

    area_code = collapse_numbers(n[0:3])
    first_three = collapse_numbers(n[3:6])
    last_four = collapse_numbers(n[6:])
    return f"({area_code}) {first_three}-{last_four}"
    
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

n = [''.join(str(n) for n in n)]






"""
Test.describe("Basic tests")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
"""

def zeros(n):
    factorial = 1
    for i in range(n):
        factorial *= i + 1

    numlist = [x for x in reversed(str(factorial))]

    count = 0
    for i in range(len(numlist)):
        if numlist[i] == str(0):
            count += 1
        else:
            break
    return count

zeros(50000)

"""
test.describe("Sample Tests")
test.it("Should pass sample tests")
test.assert_equals(zeros(0), 0, "Testing with n = 0")
test.assert_equals(zeros(6), 1, "Testing with n = 6")
test.assert_equals(zeros(30), 7, "Testing with n = 30")
"""