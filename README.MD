# Description
A simple python script to play wordle in a terminal with colored output. Uses The New York Times Wordle for daily word.

# Features:
- Uses `request` to get today's word of the day from `https://www.nytimes.com/svc/wordle/v2/[YYYY-MM-DD].json`
- Checks for input word length
- Type `giveup` to show today's word of the day
# How to run
- Install `requests`: `pip install requests`
- Type `python3 wordle.py` in the terminal while in the project folder
*or*
- Add `alias -g wordle="python3 /path/to/wordle.py` to your `.'yourshellname'rc` file to quickly access script from any terminal

# TODO
- Fix issue with displaying already guessed letters

# Plans:
- Show alphabet/keyboard with already used letters(colored)
- Make it usable with websites
- Set limit and add option to play infinitely (or vise versa)
