from Core.DieClock import DieClock
from SaveAndLoad.JSONSerializer import SerializableMixin


class WildernessTravelManager(SerializableMixin):
    def __init__(self):
        # Create Wilderness Clock
        self.WildernessClock = DieClock(5)

        # Variables
        self.WildernessLog = []

    # Log Methods
    def Log(self, TextToLog):
        self.WildernessLog.append(TextToLog)

    def WildernessClockLogString(self, ProjectedClockValue, ClockGoesOff):
        return "  The Wilderness Clock went off after " + str(ProjectedClockValue) + " days!" if ClockGoesOff else ""

    def RemoveLastLogEntry(self):
        self.WildernessLog = self.WildernessLog[:-1]

    def ClearLog(self):
        self.WildernessLog.clear()

    # Logged Methods
    def SpendDays(self, DaysSpent, Activity=None, Log=False):
        ProjectedClockValue = self.WildernessClock.Value + DaysSpent
        ClockGoesOff = self.WildernessClock.IncreaseClock(DaysSpent)
        if Log:
            if Activity is None:
                Activity = "."
            else:
                Activity = " " + Activity
                if not (Activity.endswith(".") or Activity.endswith("?") or Activity.endswith("!")):
                    Activity += "."
            self.Log("Spent " + str(DaysSpent) + " day" + ("s" if DaysSpent > 1 else "") + Activity + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))
        return ClockGoesOff

    def Move(self, TravelTime):
        ProjectedClockValue = self.WildernessClock.Value + TravelTime
        ClockGoesOff = self.SpendDays(TravelTime)
        self.Log("Moved over " + str(TravelTime) + " day" + ("s" if TravelTime > 1 else "") + "." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))

    def Forage(self):
        ProjectedClockValue = self.WildernessClock.Value + 1
        ClockGoesOff = self.SpendDays(1)
        self.Log("Spent 1 day foraging." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))

    # Unlogged Methods
    def ModifyWildernessClockCurrentValue(self, Delta):
        self.WildernessClock.ModifyCurrentValue(Delta)

    def ModifyWildernessClockMaximumValue(self, Delta):
        self.WildernessClock.ModifyMaximumValue(Delta)

    def ModifyWildernessClockThreshold(self, Delta):
        self.WildernessClock.ModifyComplicationThreshold(Delta)

    # Serialization Methods
    def SetState(self, NewState):
        self.WildernessClock = NewState["WildernessClock"]
        self.WildernessLog = NewState["WildernessLog"]

    def GetState(self):
        State = {}
        State["WildernessClock"] = self.WildernessClock
        State["WildernessLog"] = self.WildernessLog
        return State

    @classmethod
    def CreateFromState(cls, State):
        NewWildernessTravelManager = cls()
        NewWildernessTravelManager.SetState(State)
        return NewWildernessTravelManager
