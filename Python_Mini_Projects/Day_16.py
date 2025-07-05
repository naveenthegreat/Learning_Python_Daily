from abc import ABC, abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        print("Car will start")

    def stop(self):
        print("Car has been stoped")

class bike(vehicle):
    def start(self):
        print("Bike will start")

    def stop(self):
        print("Bike has been stoped")

c = car()
c.start()