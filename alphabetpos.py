def alphabet_position(text):
    text = text.lower()
    keys = {key: value for key, value in zip('abcdefghijklmnopqrstuvwxyz', range(1,27))}
    textnums = [keys[x] for x in text if x in keys]
    textnums = str(textnums).strip('[]')
    return textnums.replace(',','')


alphabet_position(text)


def iq_test(numbers):
    
    numbers = [int(x) for x in numbers.split()]
    nEven = 0
    nOdd = 0
    for index, x in enumerate(numbers):
        if x % 2 == 0:
            nEven += 1
            evenI = index
        else:
            nOdd += 1
            oddI = index

    if nEven < nOdd:
        return evenI + 1
    else:
        return oddI + 1


numbers = "2 4 7 8 10"
numbers = "1 2 2"
iq_test(numbers) 


test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")

    text = "The_pippi-is-Savage"
    text = "the_pippi-is-Savage"

def to_camel_case(text):

    text = text.replace("-", "_")
    text = text.split("_")
    newtext = [x.capitalize() for x in text]

    firstWord = str(text[0])
    if not firstWord.istitle():
        newtext[0] = str(text[0]).lower()
        
    return ''.join(newtext)
    
text = "She_stealth_warrior"

to_camel_case(text)