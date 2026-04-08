# Description
A simple python script to play wordle in a terminal with colored output. Uses The New York Times Wordle for daily word.

# Features:
- Uses `request` to get today's word of the day from `https://www.nytimes.com/svc/wordle/v2/[YYYY-MM-DD].json`
- Checks for input word length and alpha characters
- Type `giveup` to show today's word of the day
- Number of guesses limited to 6
# How to run
- Install `requests`: `pip install requests`
- Type `python3 wordle.py` in the terminal while in the project folder
*or*
- Add `alias -g wordle="python3 /path/to/wordle.py` to your shell configuration file (`.zshrc`/`.bashrc`) to quickly access script from any terminal
# TODO
- Fix issue with displaying already guessed letters
- Add tests
# Plans:
- Show alphabet/keyboard with already used letters(colored)
- Make it usable with websites
- Add option to play infinitely
