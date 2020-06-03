from Core.DiceRoller import DiceRoller
from SaveAndLoad.JSONSerializer import SerializableMixin


class DieClock(SerializableMixin):
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

    def ModifyCurrentValue(self, Delta):
        TargetValue = self.Value + Delta
        if TargetValue >= 0:
            self.Value = TargetValue

    def ModifyMaximumValue(self, Delta):
        TargetValue = self.MaximumValue + Delta
        if TargetValue >= 2:
            self.MaximumValue = TargetValue
        if self.MaximumValue <= self.ComplicationThreshold:
            self.ComplicationThreshold = self.MaximumValue - 1

    def ModifyComplicationThreshold(self, Delta):
        TargetThreshold = self.ComplicationThreshold + Delta
        if TargetThreshold < self.MaximumValue and TargetThreshold >= 0:
            self.ComplicationThreshold = TargetThreshold

    # Serialization Methods
    def SetState(self, NewState):
        self.ComplicationThreshold = NewState["ComplicationThreshold"]
        self.MaximumValue = NewState["MaximumValue"]
        self.Value = NewState["Value"]

    def GetState(self):
        State = {}
        State["ComplicationThreshold"] = self.ComplicationThreshold
        State["MaximumValue"] = self.MaximumValue
        State["Value"] = self.Value
        return State

    @classmethod
    def CreateFromState(cls, State):
        NewDieClock = cls()
        NewDieClock.SetState(State)
        return NewDieClock
