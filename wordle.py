import datetime
import requests
import tui

def get_wordle_word() -> str:
    date: datetime.date = datetime.date.today()
    url: str = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"

    response: requests.Response = requests.get(url)
    if response.status_code != 200:
        tui.error_fetching_data()
    
    data: dict = response.json()
    word_of_the_day: str = data['solution']
    return word_of_the_day
        
def is_guess_format_correct(guess: str) -> bool:
    if len(guess) != 5:
        return False
    if not guess.isalpha():
        return False
    return True

def give_feedback(guess: str, word_of_the_day: str) -> list[list[str]]:
    feedback: list[list[str]] = [[i for i in guess],
                                ["OKGREEN" if guess[i] == word_of_the_day[i] 
                                else "WARNING" if guess[i] in word_of_the_day 
                                else "" for i in range(5)]]
    return feedback

def main() -> None:
    word_of_the_day: str = get_wordle_word()
    
    times_to_play: int = 5
    for i in range(times_to_play):
        guess = tui.get_guess()
        if guess == "giveup":
            tui.print_answer(word_of_the_day)
    
        if is_guess_format_correct(guess) == False:
            tui.invalid_guess()

        feedback = give_feedback(guess, word_of_the_day)
        tui.print_feedback(feedback)

        if guess == word_of_the_day:
            tui.user_wins()
    
    tui.no_more_chances()

if __name__ == "__main__":
    main()
    