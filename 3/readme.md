## Task 2: Anagram solver
> - Get the user to input a word 
> - Create a loop that repositions each letter into a new position in the word 
> - Decide on which of the different sorting methods that you know, that might help you do this

[Run the code](https://repl.it/@minion3665/Anagram-Game)
#### Hints:
<details>
  <summary>Hint #1</summary>
  
  ```python
  import random
  ```
  
  Try importing the random module to allow chosing a random word
</details>
<details>
  <summary>Hint #2</summary>
  
  ```python
  WORD = ('apple', 'dell', 'amazon', 'microsoft', 'google')
  word = random.choice(WORD)
  correct = word
  clue = word[0] + word[(len(word)-1):(len(word))]
  letters = list(word)
  letter_guess = ''
  word_guess = ''
  store_letter = ''
  count = 0
  limit = 5

  ```
  
  Initialize starting variables
  - Pick a random word from a list of possible words
  - Allow a clue
  - Set the guess limit
</details>
<details>
  <summary>Hint #3</summary>
  
  ```python
  print('Welcome to "Amazing Anagram Game!"')
  print('You have 5 attempts at guessing letters in a word')
  print('Let\'s begin!')
  print('\n')
  ```
  
  Welcome the user to the game
</details>
<details>
  <summary>Hint #4</summary>
  
  ```python
  while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in letters:
        print('Correct!')
        letters.remove(letter_guess)
        store_letter += letter_guess
    else:
        print('Incorrect!')
    count += 1
    if count == 2:
        print('\n')
        clue_request = input('Would you like a clue? (y/n) ')
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        if clue_request == 'n':
            print('You\'re very brave! ')
  ```
  
  Start a loop to guess letters, if a letter is guessed right remove it from the letter list
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
