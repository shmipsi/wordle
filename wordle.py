import datetime
import requests
import sys

bcolors = {
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

def get_wordle_word():
    date = datetime.date.today()
    url = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"

    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    word_of_the_day = data['solution']
    return word_of_the_day
        
def check_guess(guess, word_of_the_day):
    if len(guess) != 5:
        return 1
    guess = guess.lower()
    feedback = []
    for i in range(5):
        if guess[i] == word_of_the_day[i]:
            feedback.append('OKGREEN')
        elif guess[i] in word_of_the_day:
            feedback.append('WARNING')
        else:
            feedback.append('')
    return feedback

def main():
    guess = input()

    feedback = check_guess(guess, word_of_the_day)
    if feedback == 1:
        print("Invalid guess. Please enter a 5-letter word.")
        return
    
    for i in range(5):
        print(bcolors.get(feedback[i], '') + guess[i].upper() + bcolors['ENDC'], end=' ')
    print()  # New line after feedback
    
    if guess.lower() == word_of_the_day:
        print("Congratulations! You've guessed the word of the day!")
        sys.exit()


if __name__ == "__main__":
    word_of_the_day = get_wordle_word()
    if word_of_the_day is None:
        print("Failed to retrieve the word of the day. Sorry. Try again later.")
        sys.exit()

    print("Enter your Wordle guess: ")
    while True:
        main()
    