
def tribonacci(signature, n):
    if n == 0:
        seq = []
        return seq
    elif n == 1:
        seq = signature
        seq = seq[0:1]
        print(seq)
    elif n == 2:
        seq = signature[0:2]
    elif n > 2:
        seq = signature
        iterations = n - 3
        for i in range(iterations):
            iter = i + 3
            last = seq[i:iter]
            next = sum(last)
            seq.append(next)
        return seq
    