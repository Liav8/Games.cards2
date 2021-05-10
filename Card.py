class Card: #מקבל ערך וצורה של קלף

    def __init__(self, value, suit):
        if type(value) is int and type(suit) is str:
            self.value = value
            self.suit = suit
        else:
            raise Exception("The inputs aren't valid")

# פונקציה שמדפיסה את קלף
    def __str__(self):
        return f"This card's number is: {self.value} and it's suit is: {self.suit}"

# פונקציה שמדפיסה את קלף
    def __repr__(self):
        return f"\nCard's number: {self.value}, Card's suit: {self.suit}"

# מחזירה צורה של הקלף
    def card_name(self):
        names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value == 1 or self.value > 10:
            return names[self.value]
        else:
            return False

    def __eq__(self, other):
        if type(other) is Card:
            return self.value == other.value and self.suit == other.suit
        else:
            return False






