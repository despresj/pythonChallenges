chars = ['a','b','c','d','f']
chars = ['O','Q','R','S']

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = uppercase.lower()
if chars[0].isupper():
    actual = [chars for chars in uppercase]
else:
    actual = [chars for chars in lowercase]

tester = [chars for chars in chars]

for i in range(len(actual)):
    if actual[i] == tester[0]:
        match = i
        actual = actual[match: match + len(tester) + 1]
        for j in range(len(actual)):
            if actual[j] != tester[j]:
                missing = actual[j]
                print(missing)
                break
    
