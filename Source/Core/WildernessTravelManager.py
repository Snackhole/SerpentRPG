from Core.DieClock import DieClock


class WildernessTravelManager:
    def __init__(self, SupplyPool=0, CurrentSupplyPoints=0):
        # Store Parameters
        self.SupplyPool = SupplyPool
        self.CurrentSupplyPoints = CurrentSupplyPoints

        # Create Wilderness Clock
        self.WildernessClock = DieClock(5)

        # Variables
        self.WildernessLog = []

    # Log Method
    def Log(self, TextToLog):
        self.WildernessLog.append(TextToLog)

    # Logged Methods
    def SpendSupplies(self, SupplyPointsSpent, Log=False):
        self.ModifyCurrentSupplyPointsValue(-SupplyPointsSpent)
        if Log:
            self.Log("Spent " + str(SupplyPointsSpent) + " Supply points.")

    def GainSupplies(self, SupplyPointsGained, Log=False):
        self.ModifyCurrentSupplyPointsValue(SupplyPointsGained)
        if Log:
            self.Log("Gained " + str(SupplyPointsGained) + " Supply points.")

    def SpendDays(self, DaysSpent, Log=False):
        ClockGoesOff = self.WildernessClock.IncreaseClock(DaysSpent)
        if Log:
            self.Log("Spent " + str(DaysSpent) + " days." + ("  The Wilderness Clock went off!" if ClockGoesOff else ""))
        return ClockGoesOff

    def SpendSuppliesAndDays(self, SupplyPointsAndDaysSpent, Log=False):
        self.SpendSupplies(SupplyPointsAndDaysSpent)
        ClockGoesOff = self.SpendDays(SupplyPointsAndDaysSpent)
        if Log:
            self.Log("Spent " + str(SupplyPointsAndDaysSpent) + " days and Supply points." + ("  The Wilderness Clock went off!" if ClockGoesOff else ""))
        return ClockGoesOff

    # Unlogged Methods
    def ModifySupplyPoolValue(self, Delta):
        self.SupplyPool += Delta

    def ModifyCurrentSupplyPointsValue(self, Delta):
        self.CurrentSupplyPoints += Delta

    def ModifyWildernessClockCurrentValue(self, Delta):
        self.WildernessClock.ModifyCurrentValue(Delta)

    def ModifyWildernessClockMaximumValue(self, Delta):
        self.WildernessClock.ModifyMaximumValue(Delta)
