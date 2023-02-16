# This class wraps all floors together and scans floors from bottom up to top to find first empty slot available
# and park the vehicle

from ParkingFloor import ParkingFloor


class ParkingGarage:
    def __init__(self, no_of_floors, slots_per_floor):
        self.garage = [ParkingFloor(slots_per_floor) for _ in range(no_of_floors)]
        print("Garage built ✅")

    """ check all floors from bottom up to top"""

    def park_vehicle(self, vehicle):
        for level, floor in enumerate(self.garage):
            if floor.park_vehicle(vehicle, level):
                return True

        print("Sorry All floors are full!! Check back after some time")
        return False

    def remove_vehicle(self,vehicle):
        for floor in self.garage:
            if floor.vehicle_to_slot[vehicle]:
                floor.remove_vehicle(vehicle)
                return True
        print("Woops!! Vehicle needs to be parked before removing it")
        return False
