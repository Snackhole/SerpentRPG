import random


class DiceRoller:
    def __init__(self):
        # Create Randomizer
        self.Randomizer = random.Random()

    def RollDice(self, DiceNumber=1, DieType=6, Modifier=0):
        # Results Dictionary
        Results = {}
        Results["DiceNumber"] = DiceNumber
        Results["DieType"] = DieType
        Results["Modifier"] = Modifier
        Results["Rolls"] = []
        Results["Total"] = 0

        # Roll
        for Roll in range(DiceNumber):
            CurrentRollResult = self.Randomizer.randint(1, DieType)
            Results["Rolls"].append(CurrentRollResult)

        # Total Results
        Results["Total"] = sum(Results["Rolls"]) + Modifier

        return Results

    def AverageRoll(self, DiceNumber=1, DieType=6, Modifier=0, NumberRolls=100000):
        RollResults = []
        for Roll in range(NumberRolls):
            RollResults.append(self.RollDice(DiceNumber, DieType, Modifier)["Total"])
        AverageResult = sum(RollResults) / len(RollResults)
        return AverageResult


if __name__ == "__main__":
    TestRoller = DiceRoller()
    print(TestRoller.RollDice())
    print(TestRoller.RollDice(2, 20, -3))
    print(TestRoller.AverageRoll())
    print(TestRoller.AverageRoll(1, 20, 5))
