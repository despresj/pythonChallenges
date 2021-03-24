# TODO: this needs to retun false if a 0 is in the place

def is_valid_IP(string):
    """retrun true if the string is a valad ip address
    """
    nums = [x for x in string.split(".") if x.isdigit()]
    notFourDigs = len(nums) != 4
    if notFourDigs:
        print("not four digits")
        return False
    
    numsStr = [len(x) for x in nums]
    numsInt = [int(x) for x in nums]
    numsInt = [len(str(x)) for x in numsInt]

    startsWith0 = numsStr != numsStr
    if startsWith0:
        print("starts with 0")
        return False

    greaterThan0 = min(numsInt) >= 1
    lessThan256 = max(numsInt) <= 255

    if greaterThan0 and lessThan256:
        return True
    else:
        print("too large or small")
        return False
    
string = '123.456.789.0'

is_valid_IP(string)


tests = ['12.255.56.1',
         'abc.def.ghi.jkl',
         '123.456.789.0',
         '12.34.56',
         '12.34.56 .1',
         '12.34.56.-1',
         '123.045.067.',
         '127.1.1.0',
         '0.0.0.0',
         '0.34.82.53',
         '192.168.1.300']


for test in tests:
    try:
        print(is_valid_IP(test))
    except:
        print("Broken by: " + test )