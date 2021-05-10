from unittest import TestCase
from Card import *


class TestCard(TestCase):
    # setup
    def setUp(self):
        print("A setup has been done!--------")
        self.c1 = Card(1, "Club")

    # test the valid build
    def test_cons1(self):
        self.assertIs(type(self.c1), Card)

    # test the invalid build
    def test_cons2(self):
        with self.assertRaises(Exception):
            Card(1, 1)

    # test the invalid build
    def test_cons3(self):
        with self.assertRaises(Exception):
            Card("test", "test")

    # test the invalid build
    def test_cons4(self):
        with self.assertRaises(Exception):
            Card("test", 1)

    # לבדוק האם הפעולה עובדת כמו שצריך
    def test_card_name(self):
        c2 = Card(2, "Club")
        self.assertEqual("Ace", self.c1.card_name())
        self.assertFalse(c2.card_name())

    # לבדוק האם הפעולה לא תעבוד עם קלף לא תקין
    def test_card_name2(self):
        with self.assertRaises(Exception):
            c2 = Card(2, 1)
            c2.card_name()

    # לבדוק האם הפעולה משווה שתי קלפים שווים
    def test_eq1(self):
        c2 = Card(1, "Club")
        self.assertTrue(self.c1.__eq__(c2))

    # לבדוק האם הפעולה לא משווה קלפים לא שווים
    def test_eq2(self):
        c2 = Card(1, "Diamond")
        self.assertFalse(self.c1.__eq__(c2))
        c3 = Card(2, "Club")
        self.assertFalse(self.c1.__eq__(c3))
        c4 = Card(2, "Diamond")
        self.assertFalse(self.c1.__eq__(c4))

    # לבדוק האם הפעולה לא קורסת בהכנסת לא קלף
    def test_eq3(self):
        with self.assertRaises(Exception):
            c2 = Card(1, 2)
            self.assertTrue(self.c1.__eq__(c2))



