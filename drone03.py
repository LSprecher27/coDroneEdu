from codrone_edu.drone import *
import time

drone = Drone()
drone.connect()

# Welcome to Python for Robolink! Write your Python code below.
'''drone.set_drone_LED(0, 0, 255, 100)      # blue: getting ready
drone.drone_buzzer(392, 200)
time.sleep(1)

drone.takeoff()
drone.set_drone_LED(0, 255, 0, 100)      # green: flying
drone.hover(3)

drone.set_drone_LED(255, 255, 0, 100)    # yellow: about to land
drone.land()

drone.drone_buzzer(262, 400)
drone.drone_LED_off()'''

drone.set_drone_LED(0, 255, 0, 100)
time.sleep(0.5)
drone.set_drone_LED(255, 255, 0, 100)
time.sleep(0.5)
drone.set_drone_LED(255, 0, 0, 100)
drone.drone_buzzer(440, 1000)
drone.drone_buzzer(550, 1000)
drone.drone_buzzer(900, 2000)  
drone.drone_LED_off() 
drone.disconnect()