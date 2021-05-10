from DeckOfCards import *


# פונקציה המנהלת שחקן
# שם השחקן, מספר קלפים בחבילה בהתחלה
class Player:
    def __init__(self, name="Player", num=10):
        self.deck = []
        if type(num) is int:
            if num >= 26:
                self.num = 26
            elif 0 < num:
                self.num = num
            else:
                self.num = 10
        else:
            print("The number input isn't valid, set to default of 10")
            self.num = 10
        if type(name) == str:
            self.name = name
        else:
            print("The name input isn't valid, set to default of Player")
            self.name = "Player"

# פונקציה שמקבלת חבילה ראשית ומחלקת קלפים לשחקן
    def set_hand(self, deck=[]):
        if type(deck) is DeckOfCards and len(deck.cards) >= (self.num)*2:
            for i in range(self.num):
                self.deck.append(deck.deal_one())
        else:
            raise Exception("ERROR: INVALID INPUT, Your Deck isn't a deck")

# פונקציה שמחזירה קלף רנדומלי מהיד של השחקן
    def get_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(randint(0, len(self.deck)-1))
        else:
            return False

    # פונקציה שמוסיפה קלף לשחקן
    def add_card(self, card):
        if type(card) is Card:
            self.deck.append(card)
        else:
            print("ERROR: INVALID INPUT, Your Deck isn't a deck")

# פונקציה שמדםיסה את השחקן
    def __repr__(self):
        return f"Player's name: {self.name}, his deck: {self.deck}"

# פונקציה שמדםיסה את השחקן
    def show(self):
        print(f"Player's name: {self.name}, his deck: {self.deck}")








