class vehicle:
    def move(self):
        print("vehicle is on road")

class car(vehicle):
    def move(self):                       #overriding
        print("driving on the road")

class bicycle(vehicle):
    def move(self):                         #overriding
        print("pedaling on the bicycle")

obj1 = car()
obj2 = bicycle()

obj1.move()
obj2.move()

