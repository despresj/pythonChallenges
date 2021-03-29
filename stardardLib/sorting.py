def descending_order(num):
    nums = [int(x) for x in str(num)]
    nums.sort()
    nums = nums[::-1]
    nums = [str(x) for x in nums]
    return ''.join(str(nums))    # Bust a move right h
    

num = 123456789
n = descending_order(num)

n