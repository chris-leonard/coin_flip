import random

# Single coin flip game: returns 1 if guess was correct, 0 if guess was wrong
def coin_flip_game_single():
    coin_flip_guess_string = input("Heads or tails? ")
    while 1 == 1:
        if coin_flip_guess_string.lower() == "heads":
            coin_flip_guess_num = 0
            break
        if coin_flip_guess_string.lower() == "tails":
            coin_flip_guess_num = 1
            break
        coin_flip_guess_string = input("Please guess either heads or tails: ")
    coin_flip_outcome_num = random.randint(0,1)
    if coin_flip_outcome_num == 0:
        coin_flip_outcome_string = "heads"
    else:
        coin_flip_outcome_string = "tails"
    print("The coin flip came out " + coin_flip_outcome_string + ".")
    if coin_flip_guess_num == coin_flip_outcome_num:
        print("Your guess was correct - good job!")
        return 1
    else:
        print("Unlucky, you got it wrong this time.")
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
        total_wins += coin_flip_game_single()
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
#coin_flip_game_multiple()

# Single 6-sided die roll
def die_roll_game_single():
    die_roll_guess = input("Pick a number from 1 to 6: ")
    while 1 == 1:
        if die_roll_guess in str(list(range(1, 7))):
            die_roll_guess = int(die_roll_guess)
            break
        die_roll_guess = input("Please pick a number between 1 and 6 expressed as an arabic numeral: ")
    die_roll_outcome = random.randint(1,6)
    print("I rolled a " + str(die_roll_outcome) + ".")
    if die_roll_guess == die_roll_outcome:
        print("Your guess was correct - good job!")
        return 1
    else:
        print("Unlucky, you got it wrong this time.")
        return 0

# Test
#die_roll_game_single()

# A run of dice rolls with a tally
def dice_roll_game_multiple():
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
#dice_roll_game_multiple()

# Choice between dice game and coin flip game
def coin_or_dice_game():
    coin_or_dice = input("Let's play a game of chance. Would you like to flip a coin or roll a die? ")
    total_games = 0
    total_wins = 0
    while 1 == 1:
        while 1 == 1:
            if coin_or_dice.lower() == "flip a coin":
                total_games += 1
                total_wins += coin_flip_game_single()
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
coin_or_dice_game()