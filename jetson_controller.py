import camera
import motor
import joystick
import jetson_ai


class JetsonController(object):

	def __init__(self):

		# initialize controlls
		self.camera = camera.CameraController()
		self.inferface = interface.InterfaceController()
		self.motor = motor.MotorController()
		self.joystick = joystick.JoystickController()
		