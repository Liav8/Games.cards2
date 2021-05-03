from DeckOfCards import *

# פונקציה המנהלת שחקן
# שם השחקן, מספר קלפים בחבילה בהתחלה
class Player:
    def __init__(self, name, num=10):
        self.deck = []
        self.name = name
        self.num = num
        if self.num > 26:
            self.num = 26

# פונקציה שמקבלת חבילה ראשית ומחלקת קלפים לשחקן
    def set_hand(self, deck):
        for i in range(self.num):
            self.deck.append(deck.deal_one())

# פונקציה שמחזירה קלף רנדומלי מהיד של השחקן
    def get_card(self):
        return self.deck.pop(randint(0, len(self.deck)-1))

#פונקציה שמוסיפה קלף לשחקן
    def add_card(self, card):
        self.deck.append(card)

# פונקציה שמדםיסה את השחקן
    def __repr__(self):
        return f"Player's name: {self.name}, his deck: {self.deck}"

# פונקציה שמדםיסה את השחקן
    def show(self):
        return f"Player's name: {self.name}, his deck: {self.deck}"








