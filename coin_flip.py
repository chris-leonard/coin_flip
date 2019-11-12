import random

def coin_flip():
    """
    Flips a coin, has user guess outcome, and informs them if they were correct or not.
    Returns 1 if user guesses correctly, 0 if incorrectly.
    """ 
    # Solicit user guess as a string and make it all lowercase
    coin_flip_guess = input("Take a guess: heads or tails? ")
    coin_flip_guess = coin_flip_guess.lower()

    # If guess isn't heads or tails, solicit new guess from user
    while coin_flip_guess not in ["heads", "tails"]:
        coin_flip_guess = input("Please guess either heads or tails: ")
        coin_flip_guess = coin_flip_guess.lower()

    # Flip our coin: 1 for heads, 0 for tails
    coin_flip_outcome_num = random.randint(0,1)

    # Convert outcome to string
    if coin_flip_outcome_num == 1:
        coin_flip_outcome_string = "heads"
    else:
        coin_flip_outcome_string = "tails"

    # Print outcome
    print("The coin flip came out " + coin_flip_outcome_string + ".")

    # Compare guess with outcome
    if coin_flip_gues == coin_flip_outcome_string:
        print("Your guess was correct - good job!")
        return 1
    else:
        print("Unlucky, you got it wrong this time.")
        return 0

def die_roll():
    """
    Rolls a 6-sided die, has user guess outcome, and informs them if correct or not.
    Returns 1 if user guesses correctly, 0 if incorrectly
    """
    # Solicit user guess
    die_roll_guess = input("Take a guess - pick a number from 1 to 6: ")

    # If guess isn't a number from 1 to 6, solicit a new guess
    while die_roll_guess not in str(list(range(1, 7))):
        die_roll_guess = input("Please pick a number between 1 and 6 expressed as an arabic numeral: ")
    
    # Roll die and print outcome
    die_roll_outcome = random.randint(1,6)
    print("I rolled a " + str(die_roll_outcome) + ".")

    # Verify guess with outcome
    if die_roll_guess == die_roll_outcome:
        print("Your guess was correct - good job!")
        return 1
    else:
        print("Unlucky, you got it wrong this time.")
        return 0

# Test
die_roll()

# A run of coin flip games with tally
def coin_flip_game():
    print("Let's play the coin flip game!")
    total_games = 0
    total_wins = 0
    while 1 == 1:
        total_games += 1
        total_wins += coin_flip()
        print("You've played " + str(total_games) + " times so far and won " + str(total_wins) + " times.")
        proceed_input = input("Would you like to play again? ")
        while 1 == 1:
            if proceed_input.lower() == "yes":
                print("Great, let's play again.")
                break
            if proceed_input.lower() == "no":
                print("Okay, thanks for playing.")
                return
            proceed_input = input("Please answer either yes or no: ")

# Test
#coin_flip_game()

# A run of dice rolls with a tally
def dice_roll_game():
    print("Let's play the dice roll game!")
    total_games = 0
    total_wins = 0
    while 1 == 1:
        total_games += 1
        total_wins += die_roll_game_single()
        print("You've played " + str(total_games) + " times so far and won " + str(total_wins) + " times.")
        proceed_input = input("Would you like to play again? ")
        while 1 == 1:
            if proceed_input.lower() == "yes":
                print("Great, let's play again.")
                break
            if proceed_input.lower() == "no":
                print("Okay, thanks for playing.")
                return
            proceed_input = input("Please answer either yes or no: ")

# Test
#dice_roll_game()

# Choice between dice game and coin flip game
def coin_or_dice_game():
    coin_or_dice = input("Let's play a guessing game. Would you like to flip a coin or roll a die? ")
    total_games = 0
    total_wins = 0
    while 1 == 1:
        while 1 == 1:
            if coin_or_dice.lower() == "flip a coin":
                total_games += 1
                total_wins += coin_flip()
                break
            if coin_or_dice.lower() == "roll a die":
                total_games += 1
                total_wins += die_roll_game_single()
                break
            coin_or_dice = input("Please type either 'flip a coin' or 'roll a die': ")
        print("You've played " + str(total_games) + " games so far and won " + str(total_wins) + " times.")
        proceed_input = input("Would you like to play again? ")
        while 1 == 1:
            if proceed_input.lower() == "yes":
                print("Great, let's play again.")
                break
            if proceed_input.lower() == "no":
                print("Okay, thanks for playing.")
                return
            proceed_input = input("Please answer either yes or no: ")
        coin_or_dice = input("Would you like to flip a coin or roll a die? ")
               

# Test
#coin_or_dice_game()