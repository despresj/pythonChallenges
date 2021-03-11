def high_and_low(numbers):
    numbers = [x for x in numbers.split()]
    numbers = [int(x) for x in numbers]
    numbers.sort()
    max = len(numbers)-1

    return str(numbers[0]) + " " + str(numbers[max])



