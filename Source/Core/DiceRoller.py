import random

from SaveAndLoad.JSONSerializer import SerializableMixin


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
        Results["ResultMessage"] = None

        # Roll
        for Roll in range(DiceNumber):
            CurrentRollResult = self.Randomizer.randint(1, DieType)
            Results["Rolls"].append(CurrentRollResult)

        # Total Results
        Results["Total"] = sum(Results["Rolls"]) + Modifier

        # Resolve Result Message
        if ResultMessages is not None:
            TotalString = str(Results["Total"])
            if TotalString in ResultMessages:
                Results["ResultMessage"] = ResultMessages[TotalString]

        return Results

    def AverageRoll(self, DiceNumber=1, DieType=6, Modifier=0, NumberRolls=100000):
        RollResults = []
        for Roll in range(NumberRolls):
            RollResults.append(self.RollDice(DiceNumber, DieType, Modifier)["Total"])
        AverageResult = sum(RollResults) / len(RollResults)
        return AverageResult


class DiceRollerWithPresetRolls(DiceRoller, SerializableMixin):
    def __init__(self):
        # Initialize DiceRoller
        super().__init__()

        # Preset Rolls
        self.PresetRolls = []

        # Results Log
        self.ResultsLog = []

    def RollAndLog(self, DiceNumber, DieType, Modifier):
        Results = self.RollDice(DiceNumber, DieType, Modifier)
        self.LogFromResults(Results)

    def RollAndLogPreset(self, PresetRollIndex):
        Results = self.RollPreset(PresetRollIndex)
        self.LogFromResults(Results, Prefix=self.PresetRolls[PresetRollIndex]["Name"] + ":")

    def RollAndLogAverage(self, DiceNumber=1, DieType=6, Modifier=0, NumberRolls=100000):
        AverageResult = self.AverageRoll(DiceNumber, DieType, Modifier, NumberRolls)
        self.Log("Average result of " + str(DiceNumber) + "d" + str(DieType) + ("+" if Modifier >= 0 else "") + str(Modifier) + " over " + str(NumberRolls) + " rolls:\n\n" + str(AverageResult))

    # Preset Roll Methods
    def CreatePresetRoll(self, Name, DiceNumber, DieType, Modifier, ResultMessages):
        PresetRoll = {}
        PresetRoll["Name"] = Name
        PresetRoll["DiceNumber"] = DiceNumber
        PresetRoll["DieType"] = DieType
        PresetRoll["Modifier"] = Modifier
        PresetRoll["ResultMessages"] = ResultMessages
        return PresetRoll

    def AddPresetRoll(self, Name, DiceNumber, DieType, Modifier, ResultMessages):
        self.PresetRolls.append(self.CreatePresetRoll(Name, DiceNumber, DieType, Modifier, ResultMessages))

    def RemovePresetRoll(self, PresetRollIndex):
        del self.PresetRolls[PresetRollIndex]

    def EditPresetRoll(self, PresetRollIndex, Name, DiceNumber, DieType, Modifier, ResultMessages):
        self.PresetRolls[PresetRollIndex] = self.CreatePresetRoll(Name, DiceNumber, DieType, Modifier, ResultMessages)

    def MovePresetRoll(self, PresetRollIndex, Delta):
        TargetIndex = PresetRollIndex + Delta
        if TargetIndex < 0 or TargetIndex > len(self.PresetRolls) - 1:
            return False
        CurrentPresetRoll = self.PresetRolls[PresetRollIndex]
        TargetPresetRoll = self.PresetRolls[TargetIndex]
        self.PresetRolls[TargetIndex] = CurrentPresetRoll
        self.PresetRolls[PresetRollIndex] = TargetPresetRoll
        return True

    def RollPreset(self, PresetRollIndex):
        PresetRoll = self.PresetRolls[PresetRollIndex]
        return self.RollDice(PresetRoll["DiceNumber"], PresetRoll["DieType"], PresetRoll["Modifier"], PresetRoll["ResultMessages"])

    # Log Methods
    def Log(self, TextToLog):
        self.ResultsLog.append(TextToLog)

    def LogFromResults(self, Results, Prefix=None):
        ResultsText = "" if Prefix is None else Prefix + "\n"
        ResultsText += str(Results["DiceNumber"]) + "d" + str(Results["DieType"]) + ("+" if Results["Modifier"] >= 0 else "") + str(Results["Modifier"]) + " ->\n"
        ResultsText += str(Results["Rolls"]) + ("+" if Results["Modifier"] >= 0 else "") + str(Results["Modifier"]) + " ->\n"
        ResultsText += str(Results["Total"])
        ResultsText += "" if Results["ResultMessage"] is None else "\n" + Results["ResultMessage"]
        self.Log(ResultsText)

    # Serialization Methods
    def SetState(self, NewState):
        self.PresetRolls = NewState["PresetRolls"]
        self.ResultsLog = NewState["ResultsLog"]

    def GetState(self):
        State = {}
        State["PresetRolls"] = self.PresetRolls
        State["ResultsLog"] = self.ResultsLog
        return State

    @classmethod
    def CreateFromState(cls, State):
        NewDiceRollerWithPresetRolls = cls()
        NewDiceRollerWithPresetRolls.SetState(State)
        return NewDiceRollerWithPresetRolls
