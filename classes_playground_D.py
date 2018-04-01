class Car:

    def __init__(self, clr, yr, mdl, mk, val, eng):
        self.color = clr
        self.year = yr
        self.model = mdl
        self.make = mk
        self.value = val
        self.engine = eng

    def drive_forward(self, dist):
        print("go forward {0}".format(dist))


    def drive_reverse(self):
        print("go back")


    def turn(self, dir):
        print("go {0}".format(dir))


    def start(self):
        print("On!")


    def stop(self):
        print("Off!")


ranger = Car("green", 2007, "Ford", "Ranger", 12000, 6)
ranger.start()
ranger.drive_forward(100)
ranger.turn("right")
ranger.stop()
#
#
#
# corolla = Car("black", 2010, "Toyota", "Corolla", 10000, 4)
# print(corolla.color)
# print(corolla.year)
# print(corolla.model)
