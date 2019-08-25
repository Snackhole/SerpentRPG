from Components.DieClock import DieClock


class WildernessTravelManager:
    def __init__(self, SupplyPool=0, CurrentSupplyPoints=0):
        # Store Parameters
        self.SupplyPool = SupplyPool
        self.CurrentSupplyPoints = CurrentSupplyPoints

        # Create Wilderness Clock
        self.WildernessClock = DieClock(5)

    def SpendSupplies(self, SupplyPointsSpent):
        self.CurrentSupplyPoints -= SupplyPointsSpent

    def SpendDays(self, DaysSpent):
        return self.WildernessClock.IncreaseClock(DaysSpent)

    def SpendSuppliesAndDays(self, SupplyPointsAndDaysSpent):
        self.SpendSupplies(SupplyPointsAndDaysSpent)
        return self.SpendDays(SupplyPointsAndDaysSpent)
