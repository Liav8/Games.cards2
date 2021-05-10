from Player import *
from DeckOfCards import *


# מחלקה המייצגת משחק קלפים
class CardGame:
    def __init__(self, name1="Player", name2="Player", num=10):
        self.p1 = Player(name1, num)
        self.p2 = Player(name2, num)
        self.deck = DeckOfCards()

    def __repr__(self):
        return f"This game's players are: {self.p1}.\nAnd {self.p2}"

    def show(self):
        print(f"This game's players are: {self.p1}.\nAnd {self.p2}")

    # פונקציה שיוצרת משחק חדש רק אם לא נוצר כבר ומחלקת את החפיסה בין שני השמקנים
    def new_game(self):
        if len(self.deck.cards) != 52:
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
            return f"No one won this game, A TIE!"

    # פעולה שמנהלת סיבוב ומדפיסה את המנצח בהתאם
    def round(self):
        c1 = self.p1.get_card()
        c2 = self.p2.get_card()
        changed1 = False
        print(f"\n\n{self.p1.name} card is: {c1.value} of {c1.suit}, {self.p2.name} card is: {c2.value} of {c2.suit}")
        if c1.value == 1 and c2.value == 1:
            if self.deck.names[c1.suit] > self.deck.names[c2.suit]:
                self.p2.add_card(c1)
                self.p2.add_card(c2)
                print(f"{self.p1.name} wins!")
            else:
                self.p1.add_card(c1)
                self.p1.add_card(c2)
                print(f"{self.p2.name} wins!")
        elif c1.value == 1 and c2.value > 1:
            self.p2.add_card(c1)
            self.p2.add_card(c2)
            print(f"{self.p1.name} wins!")
        elif c1.value > 1 and c2.value == 1:
            self.p1.add_card(c1)
            self.p1.add_card(c2)
            print(f"{self.p2.name} wins!")

        elif c1.value > c2.value:
            self.p2.add_card(c1)
            self.p2.add_card(c2)
            print(f"{self.p1.name} wins!")
        elif c2.value > c1.value:
            self.p1.add_card(c1)
            self.p1.add_card(c2)
            print(f"{self.p2.name} wins!")
        elif self.deck.names[c1.suit] > self.deck.names[c2.suit]:
            self.p2.add_card(c1)
            self.p2.add_card(c2)
            print(f"{self.p1.name} wins!")
        else:
            self.p1.add_card(c1)
            self.p1.add_card(c2)
            print(f"{self.p2.name} wins!")