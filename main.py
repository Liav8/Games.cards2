from CardGame import *
#יצירת משחק
game = CardGame("Liav", "Saar", 10)
game.new_game()
print(game.p1, "\n\n")
print(game.p2, "\n\n")
for i in range(10):
    game.round()
    # מה שבפלוס זה אופציה לנהל סיבוב בתוך עמוד ראשי
    # # c1 = game.p1.get_card()
    # # c2 = game.p2.get_card()
    # # print(f"P1's card is: {c1.value} of {c1.suit}, P2's card is: {c2.value} of {c2.suit}")
    # # if c1.value > c2.value:
    # #     game.p1.add_card(c1)
    # #     game.p1.add_card(c2)
    # #     print(f"{game.p1.name} wins!")
    # # elif c2.value > c1.value:
    # #     game.p2.add_card(c1)
    # #     game.p2.add_card(c2)
    # #     print(f"{game.p2.name} wins!")
    # # elif c1.suit > c2.suit:
    # #     game.p1.add_card(c1)
    # #     game.p1.add_card(c2)
    # #     print(f"{game.p1.name} wins!")
    # else:
    #     game.p2.add_card(c1)
    #     game.p2.add_card(c2)
    #     print(f"{game.p2.name} wins!")
print("\n\n\n\n")
print(f"The game winner is {game.get_winner()}")














# print(d1)
# print(len(d1.cards))
#
# d1.shuffle()
#
# for i in range(52):
#     print(d1.deal_one())
#     print(i)
#
#
#
# p1 = Player("Saaar", 12)
# p1.set_hand(d1)
# print(p1)
# print()
# print()
# print(p1.get_card())
# c1 = d1.deal_one()
# print(c1)
# p1.add_card(c1)
# print()
# print()
# print(p1)