"""
This program draws a circle's circumference by turning 3 degrees
and moving a given distance 120 times.
"""

# Importing the Turtle class from turtle module and the math module.
from turtle import Turtle
import math

# Defining drawCircle function which draws the circle.
def drawCircle(obj, centerpoint, radius):
	degree = 3
	centerpoint = (2.0 * math.pi * radius / 120)
	print ("The distance moved is", centerpoint)
	obj.home()
	obj.setheading(degree)
	count = 0
	while count <= 120:
		obj.down()
		obj.forward(2.0 * math.pi * radius / 120)
		obj.up()
		degree += 3
		obj.setheading(degree)
		count += 1

# Creating obj as Turtle Object
obj = Turtle()
centerpoint = float(input("Enter the centerpoint:"))
radius = float(input("Enter the radius:"))

# Passing values to arguments to the function drawCircle.
drawCircle(obj, centerpoint, radius)