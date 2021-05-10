from Card import *
from random import *


# מחלקה שיוצרת חבילת קלפים מסודרת (52)
class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.names = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}
        for number in range(1, 14):
            for suit in self.names.keys():
                self.cards.append(Card(number, suit))

#פעולה שמדפיסה את החבילה
    def show(self):
        print(f"This deck's cards are: {self.cards}")

# פעולה שמדפיסה את החבילה
    def __repr__(self):
        return f"This deck's cards are: {self.cards}"

# פעולה שמערבבת חפיסת קלפים
    def shuffle(self):
        shuffle(self.cards)

# פעולה שמחזירה קלף רנדומלי מהחבילה
    def deal_one(self):
        if self.cards != []:
            return self.cards.pop(randint(0, len(self.cards)-1))
        else:
            return False





