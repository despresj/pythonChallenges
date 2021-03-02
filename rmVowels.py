def disemvowel(string):
    vowels = "AEIOUaeuiu"
    string = [i for i in string if i not in vowels]
    return ''.join(string)

string = "This website is for losers LOL!"
disemvowel("This website is for losers LOL!")

def cakes(recipe, available):
    recipe_ = [i for i in recipe]
    available_ = [i for i in available]
    
    dont_have = [i for i in recipe if i not in available]
    count = []
    if len(dont_have) != 0:
        count.append(0) 
    else:
        for i in range(len(available_)):
            for j in range(len(recipe_)):
                if  available_[i] == recipe_[j]:
                    n = available[recipe_[j]] // recipe[recipe_[j]]
                    count.append(n)
                
    return min(count)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)

[i for i in recipe if i in available]


def spoonerize(words):
    new = words.split()
    first = [x for x in new[0]]
    second = [x for x in new[1]]

    first_letter = first[0]
    second_letter = second[0]

    first[0] = second_letter
    second[0] = first_letter
    return ''.join(first) + ' ' + ''.join(second)


