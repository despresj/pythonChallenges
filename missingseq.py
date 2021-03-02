def find_missing(sequence):
    dif = (sequence[-1] - sequence[0]) / len(sequence)

    numbers = range(sequence[0], sequence[-1], round(dif))
    nums = [numbers for numbers in numbers]  

    for i in range(len(sequence)):
        if sequence[i] != nums[i]:
            missing = nums[i]
            break
    
    return missing


sequence = [1, 2, 3, 4, 6, 7, 8, 9]
sequence = [1, 3, 4, 5, 6, 7, 8, 9]
find_missing(sequence)

