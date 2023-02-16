# This class represnts a single driver having a car and his due amount to pay when he leaves the parking

class Driver:
    def __init__(self, id, vehicle):
        self.id = id
        self.amount_due = 0
        self.vehicle = vehicle

    def get_vehicle(self):
        return self.vehicle

    def get_amount_due(self):
        return self.amount_due

    def get_id(self):
        return self.id

    def charge(self, amount):
        self.amount_due += amount
