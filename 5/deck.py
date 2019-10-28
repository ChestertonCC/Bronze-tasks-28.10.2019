cardNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cardSuits = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Deck:
  def __init__(self):
    self.shuffle()
  def shuffle(self):
    
