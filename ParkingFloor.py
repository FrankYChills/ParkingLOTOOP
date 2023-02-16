# This class represents a floor in a parking garage.Its responsbility are -
# 1. Declare the space in the parking floor 2. Park/remove a vehicle 3. Provide spot where a vehicle is parked


"""
0 in total slots array represents empty spot while 1 represents parked spot
return False if no space available in the current floor
"""


class ParkingFloor:
    def __init__(self, total_slots):
        self.slots = [0] * total_slots

        self.vehicle_to_slot = {}

    """ This method checks and parks vehicle if space is available 
    else returns false """

    def park_vehicle(self, vehicle, floor_level):
        vehicle_space = vehicle.get_space()
        l, r = 0, 0
        while r < len(self.slots):

            if self.slots[r] != 0:
                l = r + 1
            if r - l + 1 == vehicle_space:
                print("space available!! Parking Your vehicle..")
                for i in range(l, r + 1):
                    self.slots[i] = 1
                self.vehicle_to_slot[vehicle] = [l, r]
                print("vehicle Parked ✅")
                print(f"Your Vehicle is now parked on floor {floor_level} at slot {l}")
                return True
            r += 1
        print(f"Floor {floor_level} Full 😕")
        return False

    def remove_vehicle(self, vehicle):
        start, end = self.vehicle_to_slot[vehicle]
        for i in range(start, end + 1):
            self.slots[i] = 0
        del self.vehicle_to_slot[vehicle]
        print("Vehicle Unparked/Removed successfully ✅")

    def get_parking_space(self):
        return self.slots

    def get_vehicle_location(self, vehicle):
        return self.vehicle_to_slot[vehicle]
