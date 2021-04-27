"""Hangman Game."""
import pathlib
import random
from typing import List, Union

print(__file__)

WORDS_FILE = pathlib.Path("words.txt").cwd() / "app" / "words.txt"
STAGES = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


def get_random_word(path: str) -> str:
    """get a random word from a file containing a word on each line.

    Args:
        path (str): Path to words file.

    Returns:
        str: Random word from words file.
    """

    with open(file=path, mode="r") as fin:
        words = fin.read().splitlines()

    return random.choice(words)


def check_if_word(guess: str) -> bool:
    """If user enters more than one character assume the user is solveing the puzzle.

    Args:
        guess (str): User input.

    Returns:
        bool: True if user input is more than one character; else false.
    """
    if len(guess) > 1:
        return True
    return False


def check_letter_in_word(letter: str, word: str) -> List[int]:
    """Check if user input is in challenge word and what position(s) of the characters

    Args:
        letter (str): User input.
        word (str): Challenge word.

    Returns:
        List[int]: Index of matched characters
    """
    return [index for index, character in enumerate(word) if letter == character]


def check_user_guess(guess: str, word: str) -> bool:
    """Check if user word matches the challenge word.

    Args:
        guess (str): User input word.
        word (str): Challenge word.

    Returns:
        bool:  True on match; else false.
    """
    if guess == word:
        return True
    return False


word = get_random_word(path=WORDS_FILE)
# print(word)
display = ["_" for _ in word]
player_lives = 6


while True:
    print(STAGES[player_lives])
    if player_lives <= 0:
        print(f"you lose!\nThe word was: {word}")
        break
    print(f"{' '.join(display)}")
    user_guess = input("Please enter a letter or word: \n").lower()

    if check_if_word(guess=user_guess):
        if check_user_guess(guess=user_guess, word=word):
            print("Nailed it!")
            break
        else:
            player_lives -= 1

    else:
        letter_positions = check_letter_in_word(letter=user_guess, word=word)
        if letter_positions:
            print(letter_positions)
            for position in letter_positions:
                display[position] = user_guess
        else:
            player_lives -= 1

    if "_" not in display:
        print("Nailed it!")
        break
