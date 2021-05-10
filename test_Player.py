from unittest import TestCase
from Player import *


class TestPlayer(TestCase):
    # הגדרה
    def setUp(self):
        self.p1 = Player("HackerMan420BlazeIt", 15)
        self.d1 = DeckOfCards()
        print("A setup has been done!--------")

    # בדיקת יצירה עם משתנים תקינים
    def test_const1(self):
        self.assertEqual("HackerMan420BlazeIt", self.p1.name)
        self.assertEqual(15, self.p1.num)

    # בדיקת יצירה עם משתני ברירות מחדל
    def test_const2(self):
        p2 = Player()
        self.assertEqual("Player", p2.name)
        self.assertEqual(10, p2.num)

    # בדיקת יצירה עם משתנים לא מתאימים
    def test_const3(self):
        # בדיקה של שתי ערכים לא מתאימים
        p2 = Player(5164, "fgh")
        self.assertEqual("Player", p2.name)
        self.assertEqual(10, p2.num)

        # בדיקה של שם כמספר
        p3 = Player(5164)
        self.assertEqual("Player", p3.name)
        self.assertEqual(10, p3.num)

        # בדיקה של מספר כשם
        p4 = Player(num="fgh")
        self.assertEqual("Player", p4.name)
        self.assertEqual(10, p4.num)

        # בדיקה של מספר שלילי
        p5 = Player(num=-10)
        self.assertEqual("Player", p5.name)
        self.assertEqual(10, p5.num)

    # בדיקת ערכים תקינים
    def test_set_hand(self):
        self.p1.set_hand(self.d1)
        self.assertEqual(15, len(self.p1.deck))

    # בדיקת ערכים לא תקינים
    def test_set_hand2(self):
        with self.assertRaises(Exception):
            c1 = Card(1, "Diamond")
            self.p1.set_hand(c1)

    # בדיקת פעולה על חפיסה קטנה מן המותר
    def test_set_hand3(self):
        with self.assertRaises(Exception):
            for i in range(23):
                self.d1.deal_one()
            self.p1.set_hand(self.d1)

    # בדיקת החזרת קלך על יד ריקה
    def test_get_card(self):
        while len(self.p1.deck) > 0:
            self.p1.get_card()
        self.assertFalse(self.p1.get_card())

    # בדיקת תקינות של הוספתת קלף
    def test_add_card(self):
        c1 = self.d1.deal_one()
        oldLen = len(self.p1.deck)
        self.p1.add_card(c1)
        self.assertEqual(oldLen + 1, len(self.p1.deck))




