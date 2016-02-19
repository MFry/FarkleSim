import queue
import random, unittest
__author__ = 'michal frystacky'


class Dice:
    total_dice = 6
    dice_faces = 6

    def __init__(self):
        self.dice_faces = 6
        # TODO: Generalize dice rolls

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
    basic_100 = 0
    basic_50 = 4

    def __init__(self, players=2):
        if players < 2:
            raise Exception('Too few players playing!')
        self.total_players = players
        # TODO: Better way to define players so that the game can be played
        self.player_queue = queue.Queue()
        for _ in range(self.total_players):
            self.player_queue.put(Player())
        self.dice = Dice()

    def play_turn(self):
        player = self.player_queue.get()
        roll = self.dice.roll_dice()
        player.play_turn()

    @staticmethod
    def check_roll(dice_roll):
        # TODO: Figure out what's the best way to return the most information to avoid wasting additional processing
        result_rolls = [0] * Dice.dice_faces
        for dice in dice_roll:
            result_rolls[dice-1] += 1
        # TODO: Sort by largest number of points first to least points
        # Check for n of a kind
        pairs = 0
        triplets = 0
        for roll_count in result_rolls:
            if roll_count == 6:
                return True
            elif roll_count == 5:
                return True
            elif roll_count == 4:
                return True
            # Check for triplets
            elif roll_count == 3:
                triplets += 1
            # Check for pairs
            elif roll_count == 2:
                pairs += 1
        for i, roll_count in enumerate(result_rolls):
            if i == len(result_rolls) - 1 and roll_count == 1:
                return True
            elif roll_count == 1:
                continue
        # Check for non combination valid moves
        if roll_count[Farkle.basic_100] or roll_count[Farkle.basic_50]:
            return True
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

    def test_check_rolls(self):
        straight = [1,2,3,4,5,6]
        self.assertTrue(Farkle.check_roll(straight))
        six_of_a_kind = [random.randint(1, Dice.dice_faces)] * 6
        self.assertTrue(Farkle.check_roll(six_of_a_kind))
        five_of_a_kind = [random.randint(1, Dice.dice_faces)] * 5 + [random.randint(1, Dice.dice_faces)]
        self.assertTrue(Farkle.check_roll(five_of_a_kind))
        four_of_a_kind = [random.randint(1, Dice.dice_faces)] + [random.randint(1, Dice.dice_faces)] +[random.randint(1, Dice.dice_faces)] * 4
        self.assertTrue(Farkle.check_roll(four_of_a_kind))
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
