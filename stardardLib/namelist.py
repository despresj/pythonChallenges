"""
Format a string of names like 'Bart, Lisa & Maggie'.
"""

def namelist(names):
    names_li = [x.get('name') for x in names]
    condition = len(names_li) > 1
    if condition:
        return '{} & {}'.format(", ".join(names_li[:-1]), names_li[-1])
    elif len(names_li) == 1:
        return names[0]['name']
    else:
        return ''


namelist([])
namelist([{'name': 'Bart'}])
namelist([{'name': 'Bart'},{'name': 'Lisa'}])
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}])
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])


"""
Find the unique number
"""

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55



    def find_uniq(arr):
        min_nums = [x for x in arr if x == min(arr)]
        max_nums = [x for x in arr if x != min(arr)]
        if len(min_nums) == 1:
            return min_nums[0]
        elif len(max_nums) == 1:
            return max_nums[0]
