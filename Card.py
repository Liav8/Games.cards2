class Card: #מקבל ערך וצורה של קלף
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# פונקציה שמדפיסה את קלף
    def __str__(self):
        return f"This card's number is: {self.value} and it's suit is: {self.suit}"

# פונקציה שמדפיסה את קלף
    def __repr__(self):
        return f"\nCard's number: {self.value}, Card's suit: {self.suit}"

# מחזירה צורה של הקלף
    def card_name(self):
        names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        return names[self.value]






