import random

# Coin flip function
def flip_coin():
    flip_result = random.randint(0,1)
    if flip_result == 0:
        return "heads"
    else:
        return "tails"

# Test
#print(flip_coin())

# Solicit user guess
coin_flip_guess = input("Heads or tails? ")
coin_flip_guess_lowercase = coin_flip_guess.lower()

# Flip coin and print outcome
coin_flip_outcome = flip_coin()
print("The coin flip came out " + coin_flip_outcome + ".")

# Tell the user if they were correct
if coin_flip_guess == coin_flip_outcome:
    print("Good job! Your guess was correct")
else:
    print("Unlucky! Why not try again?")