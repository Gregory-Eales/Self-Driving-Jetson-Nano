# dependencies import 
from cv2 import *
import cv2


# initialize camera controller
class CameraController(object):

	def __init__(self):
		self.capture_save_image()
		#self.camera = VideoCapture("nvarguscamerasrc")

	def capture_image(self):

		# capture image
		self.camera = VideoCapture(0)
		s, image = self.camera.read()

		# if s is true, capture success
		if s:
			return image

		# if failure print error message
		else:
			print("Error: Unable to capture image")
			return False



	def show_webcam(self, mirror=False):
		cam = cv2.VideoCapture(0)
		while True:
			ret_val, img = cam.read()
			if mirror:
				img = cv2.flip(img, 1)
			cv2.imshow('my webcam', img)
			if cv2.waitKey(1) == 27:
				break  # esc to quit
		cv2.destroyAllWindows()

	def capture_save_image(self):
		cam = cv2.VideoCapture(0)
		while True:
			ret_val, img = cam.read()
			if mirror:
				img = cv2.flip(img, 1)
			cv2.imwrite('image', img)
			if cv2.waitKey(1) == 27:
				break  # esc to quit
		cv2.destroyAllWindows()


