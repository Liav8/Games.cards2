from Player import *
from DeckOfCards import *

#מחלקה המייצגת משחק קלפים
class CardGame:
    def __init__(self, name1, name2, num=10):
        self.p1 = Player(name1, num)
        self.p2 = Player(name2, num)
        self.deck = DeckOfCards()

    #פונקציה שיוצרת משחק חדש רק אם לא נוצר כבר ומחלקת את החפיסה בין שני השמקנים
    def new_game(self):
        if len(self.deck) != 52:
            raise Exception("You can't reset a game once it started")
        else:
            self.deck.shuffle()
            self.p1.set_hand(self.deck)
            self.p2.set_hand(self.deck)

    # פעולה שמחזירה את מנצח המשחק
    def get_winner(self):
        if len(self.p1.deck) < len(self.p2.deck):
            return self.p1
        elif len(self.p1.deck) > len(self.p2.deck):
            return self.p2
        else:
            return None
    # פעולה שמנהלת סיבוב ומדפיסה את המנצח בהתאם
    def round(self):
        c1 = self.p1.get_card()
        c2 = self.p2.get_card()
        print(f"P1's card is: {c1.value} of {c1.suit}, P2's card is: {c2.value} of {c2.suit}")
        if c1.value > c2.value:
            self.p2.add_card(c1)
            self.p2.add_card(c2)
            print(f"{self.p1.name} wins!")
        elif c2.value > c1.value:
            self.p1.add_card(c1)
            self.p1.add_card(c2)
            print(f"{self.p2.name} wins!")
        elif c1.suit > c2.suit:
            self.p2.add_card(c1)
            self.p2.add_card(c2)
            print(f"{self.p1.name} wins!")
        else:
            self.p1.add_card(c1)
            self.p1.add_card(c2)
            print(f"{self.p2.name} wins!")


