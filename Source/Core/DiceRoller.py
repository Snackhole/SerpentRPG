import random


class DiceRoller:
    def __init__(self):
        # Create Randomizer
        self.Randomizer = random.Random()

    def RollDice(self, DiceNumber=1, DieType=6, Modifier=0, ResultMessages=None):
        # Results Dictionary
        Results = {}
        Results["DiceNumber"] = DiceNumber
        Results["DieType"] = DieType
        Results["Modifier"] = Modifier
        Results["Rolls"] = []
        Results["Total"] = 0
        Results["ResultMessages"] = ResultMessages

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


class DiceRollerWithPresetRolls(DiceRoller):
    def __init__(self):
        # Initialize DiceRoller
        super().__init__()

        # Preset Rolls
        self.PresetRolls = []

    # Preset Roll Methods
    def CreatePresetRoll(self, Name, DiceNumber, DieType, Modifier, ResultMessages):
        PresetRoll = {}
        PresetRoll["Name"] = Name
        PresetRoll["DiceNumber"] = DiceNumber
        PresetRoll["DieType"] = DieType
        PresetRoll["Modifier"] = Modifier
        PresetRoll["ResultMessages"] = ResultMessages
        return PresetRoll

    def AppendPresetRoll(self, Name, DiceNumber, DieType, Modifier, ResultMessages):
        self.PresetRolls.append(self.CreatePresetRoll(Name, DiceNumber, DieType, Modifier, ResultMessages))

    def RemovePresetRoll(self, PresetRollIndex):
        del self.PresetRolls[PresetRollIndex]

    def EditPresetRoll(self, PresetRollIndex, Name, DiceNumber, DieType, Modifier, ResultMessages):
        self.PresetRolls[PresetRollIndex]["Name"] = Name
        self.PresetRolls[PresetRollIndex]["DiceNumber"] = DiceNumber
        self.PresetRolls[PresetRollIndex]["DieType"] = DieType
        self.PresetRolls[PresetRollIndex]["Modifier"] = Modifier
        self.PresetRolls[PresetRollIndex]["ResultMessages"] = ResultMessages

    def MovePresetRoll(self, PresetRollIndex, Delta):
        TargetIndex = PresetRollIndex + Delta
        if TargetIndex < 0 or TargetIndex > len(self.PresetRolls):
            return
        CurrentPresetRoll = self.PresetRolls[PresetRollIndex]
        TargetPresetRoll = self.PresetRolls[TargetIndex]
        self.PresetRolls[TargetIndex] = CurrentPresetRoll
        self.PresetRolls[PresetRollIndex] = TargetPresetRoll

    def RollPreset(self, PresetRollIndex):
        PresetRoll = self.PresetRolls[PresetRollIndex]
        return self.RollDice(PresetRoll["DiceNumber"], PresetRoll["DieType"], PresetRoll["Modifier"], PresetRoll["ResultMessages"])
