
"""

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

spinWords( "This is a test") => returns "This is a test"

spinWords( "This is another test" )=> returns "This is rehtona test"

sentence = "This is another test"

"""

def spin_words(sentence):
    sentence = sentence.split(" ")

    newlist = []
    for word in sentence:
        if len(word) > 4:
            newlist.append(word[::-1])
            print()
        else:
            newlist.append(word)
    return ' '.join(newlist)

sentence = "This is another test"
spin_words(sentence)

