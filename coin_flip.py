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


# Single coin flip game with user guess
def coin_flip_game_single():
    coin_flip_guess = input("Heads or tails? ")
    coin_flip_guess_lowercase = coin_flip_guess.lower()
    coin_flip_outcome = flip_coin()
    print("The coin flip came out " + coin_flip_outcome + ".")
    if coin_flip_guess_lowercase == coin_flip_outcome:
        print("Good job! Your guess was correct")
        return 1
    else:
        print("Unlucky - you got it wrong this time.")
        return 0

# Test
#coin_flip_game_single()

# A run of coin flip games with tally
def coin_flip_game_multiple():
    print("Let's play the coin flip game!")
    total_games = 0
    total_wins = 0
    while 1 == 1:
        total_games += 1
        #coin_flip_game = coin_flip_game_single()
        total_wins += coin_flip_game_single()
        print("You've played " + str(total_games) + " times so far and won " + str(total_wins) + " times.")
        proceed_input = input("Would you like to play again? ")
        proceed_input_lowercase = proceed_input.lower()
        if proceed_input == "yes":
            print("Great, let's play again.")
        elif proceed_input == "no":
            print("Okay, thanks for playing.")
            return

# Test
coin_flip_game_multiple()