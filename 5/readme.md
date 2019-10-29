## Task 5: Play your cards right
> - Create an array of playing cards that are random and can be used whenever you need in the rest of the program
> - Display the first card
> - Ask the user whether they think the next card is smaller or larger than the card displayed 
> - If they are correct they are then shown the next card in the list, up to a maximum of five cards
> - If they card value is the same as the previous, the game is also over
> - If they get to the end of the five cards, they have won
> - If they are incorrect the game is over
> - Ace is low, The suit order is Jack, Queen, King with King being this highest

[Run the code](https://Anagram-Game.minion3665.repl.run)
#### Hints:
<details>
  <summary>Hint #1</summary>
  
  ```python
  import random
  ```
  
  Try importing the random module to allow chosing a random card
</details>
<details>
  <summary>Hint #2</summary>
  
  ```python
cardNumbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardSuits = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Deck:
  def __init__(self):
    self.deck = []
    self.discards = []
    self.shuffle()
  @staticmethod
  def get_numbers():
    return cardNumbers
  @staticmethod
  def get_suits():
    return cardSuits
  def shuffle(self):
    deck = []
    for number in cardNumbers:
      for suit in cardSuits:
        deck.append({"number": number, "suit": suit})
    random.shuffle(deck)
    self.deck = deck
    self.discards = []

  ```
  
  Initialize starting arrays
  - Create variavles that shuffle the cards that we can use whenever needed.
  - use the ```python self.shuffle()``` variable
</details>
<details>
  <summary>Hint #3</summary>
  
  ```python
  def draw(self):
    try:
      card = self.deck.pop()
      self.discards.append(card)
      return card
    except IndexError:
      return None
  def get(self, index):
    try:
      return self.deck[-(index+1)]
    except IndexError:
      return None
  def get_discards(self):
    return self.discards
  ```
  Get deck of cards and shuffle them when needed.
  - End of deck.py file
</details>
<details>
  <summary>Hint #4</summary>
  
  ```python
  import ast
version = "a1.0.0-minimod-1"

def miniInput(inputType: type = str, *prompt: str, errorMessage: str = "You must enter a{n} {type}"):
	"""
	An input function that you always wished python had as default
	PARAMETERS:
	inputType: must be a type, determines the required type of the input. Use str to allow all input
	prompt: determines the prompt that is passed to input. Please note that "\\n>>> " will be added onto the end of the prompt
	errorMessage: the error message that will be given if the input is not of the required type. Defaults to "You must enter a{n} {type}". {Type} is replaced with the required type and {n} is replaced with the "n" if the type starts with a vowel (for use in a/an, for example).
	"""
	while True:
		inputToCheck = input(" ".join(prompt)+"\n>>> ")
		try:
			if inputToCheck:
				inputToCheck = ast.literal_eval(inputToCheck)
				return inputType(inputToCheck)
			else:
				print("You need to enter something")
		except ValueError:
			n = ""
			if inputType.__name__[0] in ["a", "e", "i", "o", "u"]:
				n = "n"
			print(errorMessage.replace("{type}", inputType.__name__).replace("{n}", n))

print("Using MiniUtils version "+version+" by MinionBAD420")
print("Please remove these credits")
print("Writing your own name makes you a coder")
  ```
  
  Miniutils.py has most of the input and text Main.py use
  - Scan user input and detect if its a real response or random text
  
</details>
<details>
  <summary>Hint #5</summary>
  
  ```python
  print('\n')
  print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
  print('These letters are: ', store_letter)

  word_guess = input('Guess the whole word: ')
  while word_guess:
    if word_guess.lower() == correct:
      print('Congrats!')
      break

    elif word_guess.lower() != correct:
      print('Unlucky! The answer was,', word)
      break

  print('\n')
  input('Press Enter to leave the program ')

  ```
  
  Let the user guess the whole word then exit
</details>
