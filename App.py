# This is the App which interacts with user.It manages payments according to the time they have parked.
# CUrrent rate for parking (just for testing) - $1 for 1 sec
# Also we are assuming that all sized cars cost the same

# The App also tracks user/driver with their initial park timing so that they can be charged when they leave
import math
import time

from ParkingGarage import ParkingGarage
from Driver import Driver
from Vehicle import Limo


class App:
    def __init__(self, parking_garage, sec_rate):
        self.sec_rate = sec_rate
        self.parking_garage = parking_garage
        self.driver_timings = {}

    """ User interacts over here"""

    def park_vehicle(self, driver):
        current_time = time.ctime(time.time())
        got_parked = self.parking_garage.park_vehicle(driver.get_vehicle())
        if got_parked:
            self.driver_timings[driver.get_id()] = [current_time, time.time()]
            print(f"Your Vehicle got parked at {current_time}")
            return True
        print("what")
        return False

    def remove_vehicle(self, driver):
        if not self.driver_timings[driver.get_id()]:
            print("Woops!! Vehicle needs to be parked before removing it 😇")
            return
        current_time = time.time()

        total_time_elapsed = math.floor(current_time - self.driver_timings[driver.get_id()][1])
        total_charge = self.sec_rate * total_time_elapsed
        driver.charge(total_charge)
        self.parking_garage.remove_vehicle(driver.get_vehicle())
        print(f"Car removed at {time.ctime(current_time)} successfully!")
        del self.driver_timings[driver.get_id()]


print("------------- Testing our parking app -------------")
print("------------- Creating a Vehicle Object(Limo) .....")
v1 = Limo()
print("------------- Creating a Driver/User ---------------")
driver1 = Driver(1, v1)
print("Initializing garage ....")
garage = ParkingGarage(4, 3)
print("Initiating app")
app = App(garage, 1)
print(f"Driver {driver1.get_id()}'s balance before : ${driver1.get_amount_due()}")
print("Park driver1 vehicle in the garage")
app.park_vehicle(driver1)
print("wait for 5 secs ..")
time.sleep(5)
print("remove from parking")
app.remove_vehicle(driver1)
print(f" Driver {driver1.get_id()}'s balance Now : ${driver1.get_amount_due()}")
print("-------------------- Testing Finished ---------------")
