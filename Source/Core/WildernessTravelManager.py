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
        self.ModifyCurrentSupplyPointsValue(SupplyPointsGained, RespectMinimum=True, RespectMaximum=True)
        if Log:
            self.Log("Gained " + str(SupplyPointsGained) + " Supply points.")

    def SpendDays(self, DaysSpent, Log=False):
        ProjectedClockValue = self.WildernessClock.Value + DaysSpent
        ClockGoesOff = self.WildernessClock.IncreaseClock(DaysSpent)
        if Log:
            self.Log("Spent " + str(DaysSpent) + " days." + ("  The Wilderness Clock went off after " + str(ProjectedClockValue) + " days!" if ClockGoesOff else ""))
        return ClockGoesOff

    def SpendSuppliesAndDays(self, SupplyPointsAndDaysSpent, Log=False):
        self.SpendSupplies(SupplyPointsAndDaysSpent)
        ProjectedClockValue = self.WildernessClock.Value + SupplyPointsAndDaysSpent
        ClockGoesOff = self.SpendDays(SupplyPointsAndDaysSpent)
        if Log:
            self.Log("Spent " + str(SupplyPointsAndDaysSpent) + " days and Supply points." + ("  The Wilderness Clock went off after " + str(ProjectedClockValue) + " days!" if ClockGoesOff else ""))
        return ClockGoesOff

    def Move(self, TravelCost):
        ProjectedClockValue = self.WildernessClock.Value + TravelCost
        ClockGoesOff = self.SpendSuppliesAndDays(TravelCost)
        self.Log("Moved with a travel cost of " + str(TravelCost) + ", spending that many days and Supply points." + ("  The Wilderness Clock went off after " + str(ProjectedClockValue) + " days!" if ClockGoesOff else ""))

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
        self.Log("Foraged for supplies, spending 1 day and Supply point." + SuppliesGainedString + ("  The Wilderness Clock went off after " + str(ProjectedClockValue) + " days!" if ClockGoesOff else ""))

    def ShortRest(self):
        pass

    def LongRest(self):
        pass

    def PurchaseSupplies(self):
        pass

    def SeekShortTermLodging(self):
        pass

    def SeekLongTermLodging(self):
        pass

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
