import queue
import random, unittest
__author__ = 'michal frystacky'


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

class Player:

    def __init__(self, ai=None):
        self.score = 0

    def play_turn(self, dice_result):
        pass

class Farkle:

    def __init__(self, players=2):
        if players < 2:
            raise Exception('Too few players playing!')
        self.total_players = players
        # TODO: Better way to define players so that the game can be played
        self.player_queue = queue.Queue()
        for _ in self.total_players:
            self.player_queue.put(Player())
        self.dice = Dice()

    def play_turn(self):
        player = self.player_queue.get()
        roll = self.dice.roll_dice()
        player.play_turn()

    @staticmethod
    def check__roll(dice_roll):
        # TODO: Figure out what's the best way to return the most information to avoid wasting additional processing
        result_rolls = 0 * Dice.dice_faces
        for dice in dice_roll:
            result_rolls[dice] += 1
        # Check for n of a kind
        for roll_count in result_rolls:
            if roll_count == 6:
                return True
            elif roll_count == 5:
                return True
            elif roll_count == 4:
                return True
        # Check for a straight
        for roll_count in result_rolls:
            if roll_count != 1:
                break
        # TODO: Check for 3 pairs and two triplets
        return False

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
'''
        def check_6_of_a_kind(dice_roll):
            check = dice_roll[0]
            for dice in dice_roll[1:]
                if check != dice:
                    return False
            return True

        def check_straight(dice_roll):
            straight = False * len(dice_roll)
            for dice in dice_roll:
                if straight[dice]:
                    return False
                else:
                    straight[dice] = True

        def check_4_of_a_kind(dice_roll):
            pass
        def check_basic(dice_roll):
            for dice_result in dice_roll:
                if dice_result == 5 or dice_result == 1:
                    return True;
            return False;
'''
