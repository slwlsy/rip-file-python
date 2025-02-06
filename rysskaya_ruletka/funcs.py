import random

import string

print(string.ascii_letters[4])

def spin(x:int):

    win_number = random.randint(1, x)

    if win_number == 1:

        return True
    
    else:
        
        return False
    
