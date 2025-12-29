def is_prime(num):
    # check if number 2
    if (num == 2):
        return True
    
    #check if number 1
    if (num == 1):
        return False
    
    for x in range(2, num):
        if (num % x == 0):
            return False
    
    return True

is_prime(7)