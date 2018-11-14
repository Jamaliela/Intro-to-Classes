######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Ela Jamali & Thomas West
# Username: lovelle & heggens             TODO: Jamalie & Westt
#
# Assignment: T13: Intro to Classes
#
# Purpose:  Demonstrate the collaboration between classes, such as using a point to create a rectangle
######################################################################
# Acknowledgements:
#
# Original code created by Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import t13_rectangle as rectangle       # notice the different ways we can import, and how that changes how we use it below
from t13_point import Point             # same as above...
import random
import turtle


def main():
    """
    Draws 25 randomly places, randomly sized, randomly colored rectangles using the turtle library.
    The code demonstrates interactions between classes, such as the use of a Point
    object to create a Rectangle object.

    :return: None
    """
    wn = turtle.Screen()
    wn.colormode(255)

    for i in range(25):
        # a point object at an (x, y) coordinate
        p = Point(random.randrange(500)-250, random.randrange(500)-250)

        # a rectangle object which starts at the point defined above
        rect = rectangle.Rectangle(p, random.randrange(i+100), random.randrange(i+100))

        # calls the draw_rectangle method of the Rectangle object
        rect.draw_rectangle(random.randrange(255), random.randrange(255), random.randrange(255), random.randrange(360), " ")

    wn.exitonclick()


if __name__ == "__main__":
    main()
