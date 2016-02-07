import random, unittest
__author__ = 'michalfrystacky'


class Dice:
    dice_faces = 6

    def __init__(self):
        self.dice_faces = 6

    @staticmethod
    def roll_dice(total_dice=6):
        results = [0] * total_dice
        for i in range(total_dice):
            results[i] = random.randint(1, Dice.dice_faces)
        return results


class TestDice(unittest.TestCase):

    def test_roll_dice(self):
        dice_stats = [0] * 6
        total_tests = 10000
        for i in range(total_tests):
            rolls = Dice.roll_dice()
            self.assertEqual(len(rolls), Dice.dice_faces)
            for roll in rolls:
                dice_stats[roll-1] += 1
        for result in dice_stats:
            self.assertAlmostEquals(result/float(total_tests*6), 1.0/6.0, 2)
