from Core.DieClock import DieClock
from SaveAndLoad.JSONSerializer import SerializableMixin


class WildernessTravelManager(SerializableMixin):
    def __init__(self):
        # Store Parameters
        self.SupplyPool = 0
        self.CurrentSupplyPoints = 0

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
    def SpendSupplies(self, SupplyPointsSpent, Log=False):
        self.ModifyCurrentSupplyPointsValue(-SupplyPointsSpent)
        if Log:
            self.Log("Spent " + str(SupplyPointsSpent) + " Supply points.")

    def GainSupplies(self, SupplyPointsGained, Log=False):
        self.ModifyCurrentSupplyPointsValue(SupplyPointsGained, RespectMinimum=True, RespectMaximum=True)
        if Log:
            self.Log("Gained " + str(SupplyPointsGained) + " Supply points.")

    def SpendDays(self, DaysSpent, Log=False):
        ProjectedClockValue = self.WildernessClock.Value + DaysSpent
        ClockGoesOff = self.WildernessClock.IncreaseClock(DaysSpent)
        if Log:
            self.Log("Spent " + str(DaysSpent) + " days." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))
        return ClockGoesOff

    def SpendSuppliesAndDays(self, SupplyPointsAndDaysSpent, Log=False):
        self.SpendSupplies(SupplyPointsAndDaysSpent)
        ProjectedClockValue = self.WildernessClock.Value + SupplyPointsAndDaysSpent
        ClockGoesOff = self.SpendDays(SupplyPointsAndDaysSpent)
        if Log:
            self.Log("Spent " + str(SupplyPointsAndDaysSpent) + " days and Supply points." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))
        return ClockGoesOff

    def Move(self, TravelCost):
        ProjectedClockValue = self.WildernessClock.Value + TravelCost
        ClockGoesOff = self.SpendSuppliesAndDays(TravelCost)
        self.Log("Moved with a travel cost of " + str(TravelCost) + ", spending that many days and Supply points." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))

    def Forage(self, HalfSucceeded, AllSucceeded):
        ProjectedClockValue = self.WildernessClock.Value + 1
        ClockGoesOff = self.SpendSuppliesAndDays(1)
        if HalfSucceeded and not AllSucceeded:
            SuppliesGainedString = "  Gained 3 Supply points."
            self.ModifyCurrentSupplyPointsValue(3, RespectMinimum=True, RespectMaximum=True)
        elif AllSucceeded:
            SuppliesGainedString = "  Gained 5 Supply points!"
            self.ModifyCurrentSupplyPointsValue(5, RespectMinimum=True, RespectMaximum=True)
        else:
            SuppliesGainedString = "  Gained no Supply points."
        self.Log("Foraged for supplies, spending 1 day and Supply point." + SuppliesGainedString + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))

    def ShortRest(self):
        ProjectedClockValue = self.WildernessClock.Value + 1
        ClockGoesOff = self.SpendSuppliesAndDays(1)
        self.Log("Spent 1 day and Supply point on a short rest." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))

    def LongRest(self):
        ProjectedClockValue = self.WildernessClock.Value + 3
        ClockGoesOff = self.SpendSuppliesAndDays(3)
        self.Log("Spent 3 days and Supply points on a long rest." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff))

    def PurchaseSupplies(self, SupplyPointsGained):
        self.GainSupplies(SupplyPointsGained)
        self.Log("Purchased " + str(SupplyPointsGained) + " Supply points.")

    def SeekShortTermLodging(self, PaidWithSupplyPoint):
        ProjectedClockValue = self.WildernessClock.Value + 1
        ClockGoesOff = self.SpendDays(1)
        if PaidWithSupplyPoint:
            self.SpendSupplies(1)
            LogString = "Spent 1 day and Supply point for short-term lodging." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff)
        else:
            LogString = "Spent 1 day and money or valuable items for short-term lodging." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff)
        self.Log(LogString)

    def SeekLongTermLodging(self, PaidWithSupplyPoints):
        ProjectedClockValue = self.WildernessClock.Value + 2
        ClockGoesOff = self.SpendDays(2)
        if PaidWithSupplyPoints:
            self.SpendSupplies(2)
            LogString = "Spent 2 days and Supply points for long-term lodging." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff)
        else:
            LogString = "Spent 2 days and money or valuable items for long-term lodging." + self.WildernessClockLogString(ProjectedClockValue, ClockGoesOff)
        self.Log(LogString)

    # Unlogged Methods
    def ModifySupplyPoolValue(self, Delta):
        self.SupplyPool += Delta

    def ModifyCurrentSupplyPointsValue(self, Delta, RespectMinimum=False, RespectMaximum=False):
        if RespectMinimum:
            self.CurrentSupplyPoints = max(0, self.CurrentSupplyPoints)
        self.CurrentSupplyPoints += Delta
        if RespectMaximum:
            self.CurrentSupplyPoints = min(self.CurrentSupplyPoints, self.SupplyPool)

    def ModifyWildernessClockCurrentValue(self, Delta):
        self.WildernessClock.ModifyCurrentValue(Delta)

    def ModifyWildernessClockMaximumValue(self, Delta):
        self.WildernessClock.ModifyMaximumValue(Delta)

    def ModifyWildernessClockThreshold(self, Delta):
        self.WildernessClock.ModifyComplicationThreshold(Delta)

    # Serialization Methods
    def SetState(self, NewState):
        self.SupplyPool = NewState["SupplyPool"]
        self.CurrentSupplyPoints = NewState["CurrentSupplyPoints"]
        self.WildernessClock = NewState["WildernessClock"]
        self.WildernessLog = NewState["WildernessLog"]

    def GetState(self):
        State = {}
        State["SupplyPool"] = self.SupplyPool
        State["CurrentSupplyPoints"] = self.CurrentSupplyPoints
        State["WildernessClock"] = self.WildernessClock
        State["WildernessLog"] = self.WildernessLog
        return State

    @classmethod
    def CreateFromState(cls, State):
        NewWildernessTravelManager = cls()
        NewWildernessTravelManager.SetState(State)
        return NewWildernessTravelManager