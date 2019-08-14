import random

# Coin flip function
def flip_coin():
    flip_result = random.randint(0,1)
    if flip_result == 0:
        return "heads"
    else:
        return "tails"

#Test
#print(flip_coin())