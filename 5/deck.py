import random

cardNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cardSuits = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Deck:
  def __init__(self):
    self.shuffle()
  def shuffle(self):
    deck = []
    for number in cardNumbers:
      for suit in cardSuits:
        deck.append({number: str(number), suit: str(suit)})
    self.deck = random.shuffle(deck)
    self.discards = []
  def draw(self):
    try:
      card = deck.pop()
      discards.append(card)
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
    
