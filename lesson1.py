n = 24

def fancyFn(n):
    if n % 2 != 0: # if n is odd
        print("Weird")        
    elif n % 2 == 0 and n >= 2 and n <= 5: # n is even and [2,5]
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20: # n is even and 
        print("Weird")
    elif n % 2 == 0 and n > 20: # n is even and greater than 2
        print("Not Weird") 
    
    

n = 18
fancyFn(n)
            
n = 4
n <= 20

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 and year % 400:
        print(true)
    
    return leap

year = int(input())
print(is_leap(year))

year = 1992
if year % 4 == 0 and year % 100 and year % 400:
        print("true")
        
        
#%%
n = 5
string = ""
for i in range(n):
    string += str(i + 1)
print(string)

    
if __name__ == '__main__':
    n = int(input())
    type(n)
    int(n)
    
# %%
def int(n):
    string = ""
    for i in range(n):
        string += str(i + 1)
    print(string)
    
int(5)

round(3.5)
sum

mo