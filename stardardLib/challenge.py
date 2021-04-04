# goal : Delete occurrences of an element if it occurs more than n times
orders = [20,37,20,21]
max_e = 3

def delete_nth(orders,max_e):
    output = []
    for order in orders:
        if output.count(order) < max_e: 
            output.append(order)
    return output

delete_nth(orders, max_e)

delete_nth([20,37,20,21], 1) # [20,37,21]
delete_nth([1,1,3,3,7,2,2,2,2], 3) # [1, 1, 3, 3, 7, 2, 2, 2]
