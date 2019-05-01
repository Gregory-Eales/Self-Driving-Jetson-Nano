# dependencies import 
from cv2 import *


# initialize camera controller
class CameraController(self):

	def __init__(self):
		self.camera = VideoCapture(0)

	def get_image(self):

		# capture image
		s, image = self.camera.read()

		# if s is true, capture success
		if s:
			return image

		# if failure print error message
		else:
			print("Error: Unable to capture image")
			return False