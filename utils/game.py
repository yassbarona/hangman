from typing import List
import random
import sys
# a 79-char ruler:
# 34567891123456789212345678931234567894123456789512345678961234567897123456789
class Hangman:

    possible_words: List[str] = ['becode',  'learning', 'mathematics',  'sessions'] 
# this 4 words are set by the assigment, but it should work with any word added
    """This attribute that contains a list of words from
    which one will be selected as the word to find"""

    word_to_find: List[str] = [] 
# it start with an empty list to later append the lettets of the word selected
    """This attribute contains a list of strings. 
    Each element will be a letter of the word."""

    lives: int = 5 # each player has 5 lives
    """This attribute contains the number of lives that the player still has
    left."""

    well_guessed_letters: List[str] = [] # it starts with an empty list that later will be filled with the amount of 
                                         # empty spaces("_") equal to the length of the word to find.
    """This attribute contains a list of strings where each element will be a letter 
    guessed by the user."""

    wrongly_guessed_letters: List[str] = []  #It starts with an an empty list that later will be 
                                             #filled with the wrongly guessed letters
    """This attribute contains a list of strings where each element will be a letter 
    guessed by the user that is not in the `word_to_find` attribute."""

    turn_count: int = 0  #It sets the count to 0 to later sum +1 every time the player tkaes a turn
    """This attribute contains the number of turns played by the player."""

    error_count: int = 0  #It sets the count to 0 to later sum +1 every time the player guesses wrong
    """This attribute contains the number of errors made by the player."""

    def __init__(self) -> None :
        word: str = random.choice(self.possible_words)  #selct random word
        for i in word:  #appends every character of word to the empty lists
            self.word_to_find.append(i)
            self.well_guessed_letters.append("_")
        print("WELCOME TO THE HANGMAN GAME!!!!!")
    """ This method sets up the game selecting a random word, adding it to the 
    word_to_find attribute and creating the 'blank' spaces that will later be replaced
    at the well_guessed_letters attribute """


    def play(self) -> str:
        letter = input("Please enter a letter:_") #It asks user ot introduce a letter
        if len(letter) != 1:  # It sets up a condition to be sure only letters are valid
            print("Only 1 letter is valid as input")
            self.play()  # time to start playing
        else:
            self.turn_count += 1  # It adds 1 to user's turns counting
            if letter in self.word_to_find:  # Validates if input exists in the word_to_find list
                indexes = []  # empty list to add the indexes of letter that matches the user's input
                for l in range(len(self.word_to_find)):  # iterate over index of each metter in word_to_find
                    if self.word_to_find[l] == letter:  # if the value of the index matches the input letter
                        indexes.append(l)  # it adds it to the indexes list
                for index in indexes:  # the value of every index of the list replaces the "_"
                    self.well_guessed_letters[index] = letter
            else:
                self.wrongly_guessed_letters.append(letter) #adds word to the wrongly_guessed_list if it is not in word_to_find
                self.error_count += 1  # It adds 1 to the error count
                self.lives -= 1  # It takes 1 life from the user
                print("WRONG... Try again \n")
        """This method asks the player to enter a letter. 
        Player is not allowed to type something else than a letter, and not more than a letter. 
        If the player guessed a letter well, it is added to the `well_guessed_letters` list. 
        If not, it is added to the `wrongly_guessed_letters` list and 1 is added to `error_count`."""

    def start_game(self): 
        while self.word_to_find != self.well_guessed_letters  or self.error_count != 0: # Loop to continue if either the word_to_find is not the same as the word in 
            self.play()
            print("Correct letters: " + "".join(self.well_guessed_letters) + "\n"
            + "incorrect letters: "+ ", ".join(self.wrongly_guessed_letters) + "\n"
            + f"you have only {self.lives} lives left" + "\n" + f"You made {self.error_count} errors in {self.turn_count} turns \n")
            if self.word_to_find == self.well_guessed_letters:  # condition to set if the user won
                self.well_played()  
            elif self.lives == 0: # condition to set if the user lost
                self.game_over()
                """ This method:
                - will call `play()` until the game is over (because the use guessed the word or because of a game over).
                - will call `game_over()` if `lives` is equal to 0.
                - will call `well_played()` if all the letter are guessed.
                - will print `well_guessed_letters`, `bad_guessed_letters`, `life`, `error_count` and `turn_count` at the end of each turn."""


    def game_over(self) -> str:
        print("LOOOOSSEERRR!!!!... You got Hanged -\_(✖╭╮✖)_/- \nGAME OVER..." )
        sys.exit()
        """this methods sets the eng of the gamr if user lost"""

    def well_played(self) -> str:
        winning_word = "".join(self.word_to_find)
        print(f"CONGRATS!!! You found the word {winning_word.upper()} in {self.turn_count} turns with {self.error_count} errors! °\(❛ᴗ❛)/° ")
        sys.exit()
        """" this methods sets the eng of the gamr if user lost and will print
        `You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!`."""