import random


# Define a function to print the game title and instructions
def print_title():
    print("=== Climate Action Heroes ===\n")
    print("You are a climate action hero, and your mission is to save the planet from environmental disaster.\n")
    print("You will be presented with a series of challenges, and you must make choices to overcome them.\n")


# Define a function to get the player's name
def get_player_name():
    name = input("What is your name? ")
    print(f"\nWelcome, {name}! Let's get started.\n")
    return name


# Define a function to generate a random number between 1 and 10
def generate_random_number():
    return random.randint(1, 10)


# Define a function to check if the player's guess is correct
def check_guess(guess, number):
    if guess == number:
        print("Correct! You saved the planet!")
        return True
    else:
        print("Incorrect. The planet is doomed.")
        return False

    # Define a function for the recycling challenge
def recycling_challenge():
        print("Challenge: Recycling")
        print("You come across a pile of waste that needs to be sorted for recycling.")
        print("You have 3 bins labeled 'paper', 'plastic', and 'glass'.")
        print("You must sort the items correctly to pass the challenge.\n")
        items = ["newspaper", "magazines", "cardboard", "pens", "bags", "containers", "bottles", "jars", "cups"]
        random.shuffle(items)
        counter_variable = 0
        list_dict = {
            "paper": ["newspaper", "magazines", "cardboard"],
            "plastic": ["pens", "bags", "containers"],
            "glass": ["bottles", "jars", "cups"]
        }
        for item in items:
            category = None
            for bin_label, bin_items in list_dict.items():
                if item in bin_items:
                    category = bin_label
                    break
            if category is None:
                print(f"Error: {item} not found in any category.")
                continue
            bin_choice = input(f"Which bin should {item} go in? ")
            if bin_choice.lower() == category:
                counter_variable += 1
                print(f"Correct! {item} goes in the {category} bin.")
            else:
                print(f"Incorrect. {item} does not go in the {bin_choice.lower()} bin.")
        if counter_variable >= 6:
            print("Congratulations! You have passed the recycling challenge.")
            return True
        else:
            print("You have failed the recycling challenge.")
            return False
    # Define a function for the transportation challenge
def transportation_challenge():
        print("Challenge: Transportation")
        print("You need to travel to a nearby town to attend a climate action protest.")
        print("You have three options: drive a car, take a bus, or ride a bike.")
        print("Choose wisely to minimize your carbon footprint.\n")
        choice = input("How do you want to travel? ")
        if choice.lower() == "car":
            print("Driving a car produces a lot of emissions, which contribute to climate change.")
            print("You have failed the transportation challenge.")
            return False
        elif choice.lower() == "bus":
            print("Taking a bus is a good option, as it can transport many people at once.")
            print("However, buses still produce emissions and can get stuck in traffic.")
            print("You have partially passed the transportation challenge.")
            return True
        elif choice.lower() == "bike":
            print("Riding a bike is the most sustainable option, as it produces no emissions.")
            print("However, it may take longer to reach your destination.")
            print("Congratulations! You have passed the transportation challenge.")
            return True
        else:
            print("Invalid choice. You have failed the transportation challenge.")
            return False
def main():
    print_title()
    player_name = get_player_name()
    score = 0

    # Recycling challenge
    if recycling_challenge():
        print("You have earned 1 point!")
        score += 1
    else:
        print("You failed to earn a point for the recycling challenge.")

    # Transportation challenge
    if transportation_challenge():
        print("You have earned 1 point!")
        score += 1
    else:
        print("You failed to earn a point for the transportation challenge.")

    # Number guessing challenge
    print("Challenge: Number guessing")
    print("You must guess a number between 1 and 10 to save the planet.")
    random_number = generate_random_number()
    guesses = 3
    while guesses > 0:
        guess = int(input("Guess a number: "))
        if check_guess(guess, random_number):
            print("You have earned 1 point!")
            score += 1
            break
        else:
            guesses -= 1
            print(f"You have {guesses} guesses left.")
    if guesses == 0:
        print("You failed to earn a point for the number guessing challenge.")

    # Final score
    print(f"\nCongratulations, {player_name}! You have completed all challenges.")
    print(f"Your final score is {score} out of 3.")
main()