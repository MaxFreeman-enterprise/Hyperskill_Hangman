import random

ATTEMPTS_NUMBER = 8


def run_game():
    lst = ["python", "java", "kotlin", "javascript"]
    # set_ = set(lst)  # <---- the better solution guys
    # answer = set_.pop()
    answer = random.choice(lst)

    # hint = answer[:3] + "-" * len(answer[3:])

    displayed_word = ["-"] * len(answer)

    answer_letters = frozenset(answer)

    remaining_attempts = ATTEMPTS_NUMBER

    past_guesses = set()

    print("H A N G M A N")

    while remaining_attempts > 0:

        print()
        print("".join(displayed_word))
        user_guess = input("Input a letter: ")

        if len(user_guess) != 1:
            print("You should input a single letter")

        elif not user_guess.islower() or not user_guess.isalpha():
            print("Please enter a lowercase English letter")

        elif user_guess in past_guesses:
            print("You've already guessed this letter")

        elif user_guess in answer_letters and user_guess not in displayed_word:
            for j in range(len(answer)):
                if answer[j] == user_guess:
                    displayed_word[j] = user_guess

            if "".join(displayed_word) == answer:
                print("You guessed the word!")
                break

        elif user_guess in answer_letters and user_guess in displayed_word:
            remaining_attempts -= 1
            print("No improvements")

        else:
            remaining_attempts -= 1
            print("That letter doesn't appear in the word")
        past_guesses.add(user_guess)

    if "".join(displayed_word) == answer:
        print("You survived!")
    else:
        print("You lost!")


def read_user_action():
    user_action = ""

    while user_action != "play" and user_action != "exit":
        user_action = input("""Type "play" to play the game, "exit" to quit: """)
    return user_action


while True:
    user_action = read_user_action()

    if user_action == "exit":
        exit()

    elif user_action == "play":
        run_game()

    else:
        pass
