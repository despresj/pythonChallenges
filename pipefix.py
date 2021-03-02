def pipe_fix(nums):
    seq = range(nums[0], nums[-1] + 1)
    new = [seq for seq in seq]
    return new

def stringy(size):
    out = []
    for i in range(size):
        if i % 2 == 0:
            out.append(1)
        else: out.append(0)
    ret = [str(out) for out in out]
    final = int(''.join(ret))
    return final

stringy(3)

for i in range(5, 9):
    print('- __0' + str(i) + ':00 - 0'+str(i+1)+':00__ :')

for i in range(9, 23):
    print('- __' + str(i) + ':00 - '+str(i+1)+':00__ :')
    
    
# Factorial maket

nums = [1, 2, 3, 4]

[nums for nums in nums]

output = 1
for i in range(len(nums)):
    output *= nums[i]
    print(output)
    
def positive_sum(arr):
    out = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            out += arr[i]
    return out

arr = [5,2,3,-4]

[x for x in arr if x > 0]

positive_sum()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "an" in x]

print(newlist)


string = 'world'
string[::-1]

new = [x ]

s = 'eloquent'

new = [x for x in s]
del new[0]
del new[-1]
return ''.join(new)
print(new)