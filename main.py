#import jetson_controller
#import threading
import camera

#jet = jetson_controller.JetsonController()

# main script loop

running = True

# is threading neccesary?
# initialize threads

# 1. interface thread
# 2. ai thread
# 3. motor thread
# 4. ultrasonic thread
# 5. camera thread
# 6. joystick thread

while running:

	running = False

	# IDLE INTERFACE MODE:
	# 	-check interface input
	# 	-update interface output
	#	-update mode frome input
	
	# AUTONOMOUS MODE:
	#	-check ultrasonic proximity
	#	-check for remote kill signal
	#	-capture image
	#	-generate motor output from image and ai model
	#	-activate motors

	# DATA CAPTURE MODE:
	#	-get joystick output
	# 	-capture image
	# 	-save data
	#	-convert to motor controll
	#	-activate motors
	#	-check kill signal

	# DIAGNOSTIC MODE:
	#	-check image capture
	#	-check ultrasonic capture
	#	-check remote controll
	# 	-check joystick

	pass



cam = camera.CameraController()

























