######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Ela Jamali & Thomas West
# Username: lovelle & heggens             TODO: Jamalie & Westt
#
# Assignment: T13: Intro to Classes
#
# Purpose:  Demonstrate the collaboration between classes, such as using a point to create different shapes
######################################################################
# Acknowledgements:
#
####################################################################################

import t13_shape as Shape       # importing shape
from t13_point import Point      # importing Point
import random
import turtle


def main():
    """
    Draws 25 randomly places, randomly sized, randomly colored shapes using the turtle library.
    The code demonstrates interactions between classes, such as the use of a Point
    object to create a shape object.

    :return: None
    """
    wn = turtle.Screen()
    wn.colormode(255)

    for i in range(25):
        # a point object at an (x, y) coordinate
        p = Point(random.randrange(500)-250, random.randrange(500)-250)

        # a my_shape object which starts at the point defined above
        my_shape = Shape.Shape(p, random.randrange(12), random.randrange(100))

        # calls the draw_shape method of the my_shape object
        my_shape.draw_shape(random.randrange(255), random.randrange(255), random.randrange(255), random.randrange(360))

    wn.exitonclick()


if __name__ == "__main__":
    main()
