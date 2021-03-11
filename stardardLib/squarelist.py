def square_digits(num):
    nums = [int(x) * int(x) for x in str(num)]
    out = ''.join([str(x) for x in nums])
    return int(out)

