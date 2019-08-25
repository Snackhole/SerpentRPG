from Components.DiceRoller import DiceRoller


class DieClock:
    def __init__(self, ComplicationThreshold=10, MaximumValue=21):
        # Store Parameters
        self.ComplicationThreshold = ComplicationThreshold
        self.MaximumValue = MaximumValue

        # Initial Value
        self.Value = 0

        # Dice Roller
        self.DiceRoller = DiceRoller()

    def IncreaseClock(self, ValueIncrease=1):
        self.Value += ValueIncrease
        if self.Value > self.ComplicationThreshold:
            ClockRoll = self.DiceRoller.RollDice(DieType=self.MaximumValue - 1)["Total"]
            if ClockRoll < self.Value:
                self.Value = 0
                return True
        return False
