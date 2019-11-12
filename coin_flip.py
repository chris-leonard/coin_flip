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
    if coin_flip_guess == coin_flip_outcome_string:
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


def coin_or_die_game():
    """
    Asks user to either flip a coin or roll a die and guess the outcome.
    Allows user to play multiple games and counts games played and wins.
    """
    # Initialise counters
    total_games = 0
    total_wins = 0

    print("Let's play a guessing game.")

    while 1 == 1: 
        total_games += 1

        # Solicit game choice
        game_choice = input("Would you like to flip a coin or roll a die? ").lower()

        # Solicit new response if not in required form
        while game_choice not in ["flip a coin", "roll a die"]:
            game_choice = input("Please type either 'flip a coin' or 'roll a die': ").lower()
        
        # Play game and update counters
        if game_choice == "flip a coin":
            total_wins += coin_flip()
        else:
            total_wins += die_roll()
        
        # Print running tally
        print("You've played " + str(total_games) + " games so far and won " + str(total_wins) + " times.")

        # Ask to play again
        proceed_input = input("Would you like to play again? ").lower()

        while proceed_input not in ["yes", "no"]:
            proceed_input = input("Please answer either yes or no: ").lower()
        
        if proceed_input == "yes":
            print("Great, let's play again.")
        else:
            print("Okay, thanks for playing.")
            break

# Run game
coin_or_die_game()