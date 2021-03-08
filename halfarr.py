"""
find index where the cumulitive sum is equal to the reverse cumulitive sum
eg [1,2,3,4,3,2,1] at the third index 
sum([1,2,3,4]) = sum([4,3,2,1])
"""
def find_even_index(arr):
    boolvec = []
    for i in range(len(arr)):
        condition = sum(arr[:i+1]) == sum(arr[i:])
        boolvec.append(condition)
        if condition:
            return i

    if sum(boolvec) == 0:
        return -1
    
find_even_index(arr = [1,2,3,4,3,2,1])

"""
print true if value is a 'narcissistic number'
the sum of digits to the exponent of the number of digits
eg: 371 has 3 digits so 3^3 + 7^3 + 1^3 = 371
"""
def narcissistic(value):
    exponenet = len(str(value))
    nums = [int(x)**exponenet for x in str(value)]
    if sum(nums) == value:
        return True
    else:
        return False
    
narcissistic(value = 7)
narcissistic(value = 371)
narcissistic(value = 4887)


"""
find prime not done
TODO: make this work for negitive
"""
def is_prime(num):
    
    for i in divisors:
        if num % i == 0:
            return False
            break
    return True


def is_prime(num):
    bools = any([num%x == 0 for x in range(2, 10) if x != num])
    if num > 0:
        return bools
    else:
        return not bools


