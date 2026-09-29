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
drone.takeoff()
drone.move_forward(65, "in", 0.5)
drone.turn_right()

drone.move_forward(24, "in", 0.5)
drone.turn_left()

drone.move_forward(60, "in", 0.5)
drone.turn_right()

drone.move_forward(52, "in", 0.5)

drone.hover(1)

drone.land()
drone.disconnect()
