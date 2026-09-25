from codrone_edu.drone import *

drone = Drone()
drone.connect()

# Welcome to Python for Robolink! Write your Python code below.
battery = drone.get_battery()
print("Battery:", battery, "%")

drone.set_drone_LED(255, 0, 0, 100)   

drone.takeoff()

drone.hover(3)

drone.land() 

drone.drone_buzzer(440, 500)   

drone.disconnect()