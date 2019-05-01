# dependencies import 
import camera
import motor
import joystick
import jetson_ai


class JetsonController(object):

	# initialize
	def __init__(self):

		# initialize controlls
		self.camera = camera.CameraController()
		self.inferface = interface.InterfaceController()
		self.motor = motor.MotorController()
		self.joystick = joystick.JoystickController()
		self.ai = jetson_ai.JetsonAI()
		self.ultrasonic = ultrasonic.UltrasonicController()

	# run autonomous self driving
	def autonomous_main(self):
		pass

	# run main data collection loop
	def data_collection_main(self):
		pass

	# saves data pair
	def save_data(self, image, input):
		pass