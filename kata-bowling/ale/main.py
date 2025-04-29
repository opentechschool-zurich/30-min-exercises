# https://docs.python.org/3/library/unittest.html
# https://kata-log.rocks/bowling-game-kata

import unittest

# from bowling import Bowling

class Bowling:
    def __init__(self):
        self.roll_counter = 0
        self.current_score = 0
        self.spare = 0
        self.strike = False

    def roll(self, pins_knocked_down):
        if self.roll_counter == 20:
            # there could be an extra roll
            if self.strike or self.spare == 10:
                self.current_score += pins_knocked_down * 2
            self.strike = False
            self.spare == 0
            return
        self.roll_counter += 1
        if self.roll_counter % 2 == 1:
            if self.strike:
                self.current_score += pins_knocked_down *2
            elif self.spare == 10:
                self.current_score += pins_knocked_down *2
            else:
                self.current_score += pins_knocked_down
            if pins_knocked_down == 10:
                self.strike = True
            else:
                self.strike = False
                self.spare = pins_knocked_down
        else:
            if self.strike:
                self.current_score += pins_knocked_down * 2
            else:
                self.spare += pins_knocked_down
                self.current_score += pins_knocked_down

    def score(self):
        return self.current_score
    

class TestBowling(unittest.TestCase):
    def test_zero_score_when_rolling_0_pins(self):
        bowling = Bowling()
        bowling.roll(0)
        self.assertEqual(bowling.score(), 0)
    def test_10_score_when_strike_in_first_roll(self):
        bowling = Bowling()
        bowling.roll(10)
        self.assertEqual(bowling.score(), 10)
    def test_4_than_5_score_in_two_rolls(self):
        bowling = Bowling()
        bowling.roll(4)
        bowling.roll(5)
        self.assertEqual(bowling.score(), 9)
    def test_4_and_6_then_2_and_3_trigger_spare_of_2(self):
        bowling = Bowling()
        bowling.roll(4)
        bowling.roll(6)
        bowling.roll(2)
        bowling.roll(3)
        self.assertEqual(bowling.score(), 17)
    def test_10_and_4_then_2_and_3_trigger_strike_of_4_and_2(self):
        bowling = Bowling()
        bowling.roll(10)
        bowling.roll(4)
        bowling.roll(2)
        bowling.roll(3)
        self.assertEqual(bowling.score(), 10 + 4 * 2 + 2 * 2 + 3)
    def test_10_and_10_then_10_and_3_then_2_and_1_trigger_strike_twice(self):
        bowling = Bowling()
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(3)
        bowling.roll(2)
        bowling.roll(1)
        self.assertEqual(bowling.score(), 10 + 10 * 2 + 10 * 2 + 3 * 2 + 2 * 2 + 1)
    


if __name__ == '__main__':
    unittest.main()
