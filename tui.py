import sys

bcolors: dict[str, str] = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

def error_fetching_data() -> None:
    print("Failed to retrieve the word of the day. Sorry. Try again later.")
    sys.exit()

def print_answer(word_of_the_day: str) -> None:
    print(f"The word of the day was: {word_of_the_day.upper()}")
    sys.exit()

def invalid_guess() -> None:
    print("Invalid guess. Please try again.")

def user_wins() -> None:
    print("Congratulations! You've guessed the word of the day!")
    sys.exit()

def no_more_chances() -> None:
    print("Sorry, you've used all your chances. Better luck next time!")
    sys.exit()

def print_feedback(feedback: list[list[str]]) -> None:
    for i in range(5):
        print(bcolors.get(feedback[1][i], '') + feedback[0][i].upper() + bcolors['ENDC'], end=' ')
    print()  # New line after feedback
    return

def get_guess() -> str:
    return input("Enter your guess: ").lower()