from unittest import TestCase, mock
from Player import *
from CardGame import *
from DeckOfCards import *
from Card import *


class TestCardGame(TestCase):
    def setUp(self):
        self.p1 = Player()
        self.p2 = Player("Niv", 24)
        self.game1 = CardGame(name2=self.p2.name, num=self.p2.num)
        self.game1.new_game()

    # בדיקה להאם אורך החבילה של P2 נכנס למשחק בתור תכונה של שחקן 1
    def test_ConstDeckP1deck(self):
        self.assertEqual(len(self.game1.p1.deck), self.p2.num)

    # בדיקה להאם השם הברירת מחדל נכנס למשחק בתור תכונה של שחקן 1
    def test_ConstDeckP1name(self):
        self.assertEqual(self.game1.p1.name, "Player")

    # בדיקה שמראה שאורך החבילה של שחקן 2 נקבע על פי המספר שהוכנס ל "new game"
    def test_ConstDeckP2deck(self):
        self.assertEqual(len(self.game1.p2.deck), self.p2.num)

    # בדיקה להאם השם הברירת מחדל נכנס למשחק בתור תכונה של שחקן 1
    def test_ConstDeckP2name(self):
        self.assertEqual(self.game1.p2.name, self.p2.name)

    # בדיקה שמראה לי שאם אני מנסה לאפס משחק לאחר שהתחיל תעלה לי שגיאה שקבעתי מראה
    def test_NewGame1(self):
        with self.assertRaises(Exception):
            self.game.new_game()

    # בדיקה שבודקת שכאשר אני מתחיל משחק החבילה שלו מתערבבת
    def test_NewGame2(self):
        game2 = CardGame()
        DeckB4Shuffle = game2.deck.cards.copy()
        game2.new_game()
        self.assertNotEqual(game2.deck.cards, DeckB4Shuffle)




    # בודק האם המנצח הוא שחקן אחד כאשר לשחקן אחד יש פחות קלפים בחבילה
    def test_get_winnerp1(self):
        self.game.p1.get_card()
        self.assertIs(self.game.p1, self.game.get_winner())

    # בודק האם המנצח הוא שחקן שתיים כאשר לשחקן שתיים יש פחות קלפים בחבילה
    def test_get_winnerp2(self):
        self.game.p2.get_card()
        self.assertIs(self.game.p2, self.game.get_winner())

    # בודק האם אין מנצח אם לשניהם יש את אותו מספר קלפים בחבילה
    def test_get_winnerNone(self):
        self.assertIs(None, self.game.get_winner())


    # בדיקה לאם שחקן מספר 1 מנצח בסיבוב אם המספר קלף שווה אך לשחקן מספר 1 חליפת קלף גבוהה יותר
    def test_round1(self):
        self.game1.p1.deck = [Card(12, "Club")]
        self.game1.p2.deck = [Card(12, "Heart")]
        self.game1.round()
        self.assertTrue(len(self.game1.p2.deck) > len(self.game1.p1.deck))

    # בדיקה לאם שחקן מספר 2 מנצח בסיבוב אם המספר קלף שווה אך למספר 2 חליפת קלף גבוהה יותר
    def test_round2(self):
        self.game1.p2.deck = [Card(12, "Club")]
        self.game1.p1.deck = [Card(12, "Heart")]
        self.game1.round()
        self.assertTrue(len(self.game1.p2.deck) < len(self.game1.p1.deck))

    # בדיקה לאם שחקן מספר 1 מנצח בסיבוב אם הערך של הקלף שלו יותר גדול
    def test_round3(self):
        self.game1.p1.deck = [Card(12, "Club")]
        self.game1.p2.deck = [Card(10, "Heart")]
        self.game1.round()
        self.assertTrue(len(self.game1.p2.deck) > len(self.game1.p1.deck))

    # בדיקה לאם שחקן מספר 2 מנצח בסיבוב אם הערך של הקלף שלו יותר גדול
    def test_round4(self):
        self.game1.p2.deck = [Card(12, "Club")]
        self.game1.p1.deck = [Card(10, "Heart")]
        self.game1.round()
        self.assertTrue(len(self.game1.p2.deck) < len(self.game1.p1.deck))