from codrone_edu.drone import *

drone = Drone()
drone.connect()
'''
# Welcome to Python for Robolink! Write your Python code below.
drone.takeoff()
drone.hover(1)

for i in range(4):                  # do this four times
    drone.move_forward(20, "cm", 1)
    drone.turn_left()               # turn 90 from where it is facing now
'''
drone.move_forward(83, "in", 1)
drone.turn_left(degree, timeout)

drone.move_forward(43, "in", 1)
drone.turn_right()

drone.move_forward(66, "in", 1)
drone.turn_right()

drone.move_forward(91, "in", 1)

drone.hover(1)

drone.land()
drone.disconnect()
