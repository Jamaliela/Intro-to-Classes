######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Ela Jamali & Thomas West
# Username: lovelle & heggens             TODO: Jamalie & Westt
#
# Assignment: T13: Intro to Classes
#
#
# Purpose: A class for creating rectangles. Collaborates with the Points class
######################################################################
# Acknowledgements:
#
####################################################################################

import turtle


class Shape:
    """
    A class that will draw shapes using the turtles. This class will manipulate position , side and length of the sides
    """

    def __init__(self, posn, s, l):
        """
         Initialize shapes at posn, with a number of sides s, length of the sides l

        :param posn: a Point object representing the starting point of the shape
        :param s: the shapes' number of sides
        :param l: the sides' length
        """
        self.start_point = posn          # A Point object to hold the bottom left corner of the shape
        self.num_sides = s
        self.side_length = l
        self.turt = None

    def __str__(self):
        """
        Overridden string class which allows the user to use str() to print cleanly.

        :return: A formatted string
        """

        return "({0}, {1}, {2})".format(self.start_point, self.num_sides, self.side_length)

    def draw_shape(self, r=0, g=0, b=0, angle=0):  # black is the default color
        """
        Instantiates a Turtle object and draws shapes on the Screen at an angle.


        :param r: the red channel
        :param g: the green channel
        :param b: the blue channel
        :param angle: the angle to draw the turtle
        :return: None
        """
        self.turt = turtle.Turtle()
        self.turt.speed(0)
        self.turt.color(r, g, b)
        self.turt.penup()

        # self.start_point refers to a Point object, so self.start_point.x refers to the x-coordinate;
        # self.start_point.y refers to the y-coordinate
        self.turt.goto(self.start_point.x, self.start_point.y)

        # rotates to turtle by angle degrees
        self.turt.left(angle)
        self.turt.showturtle()
        self.turt.pendown()

        # draws the shape to the screen
        for i in range(self.num_sides):
            self.turt.forward(self.side_length)
            self.turt.left(360 / self.num_sides)

        self.turt.hideturtle()
# end class
