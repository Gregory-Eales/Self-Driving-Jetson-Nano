from inputs import get_gamepad
import time
import numpy as np

class JoystickController(object):

	def __init__(self):

		self.directions = ["ABS_RZ", "ABS_Z"]
		self.right_state = 0
		self.left_state = 0
		self.pi = 3.14159

	def get_movement_vector(self):
		return self.forward_state, self.backward_state
	
	def normalize(self, n):
		return (n - 127.5)/127.5

	def transform(self, forward, backward):

		left = 0
		right = 0
		
		theta = np.arctan(forward/backward)

		theta = theta/self.pi
		
		if theta < 0.5: 
		
	def get_inputs(self):
		
		# event attributes:
		# event.ev_type, event.code, event.state

		output = [0,0]
		
		events = get_gamepad()
		forward = None
		backward = None
		
		for event in events:

			if event.code == self.directions[0]:
				forward = -self.normalize(event.state)
			
			if event.code == self.directions[1]:
				backward = self.normalize(event.state)
	
		if forward == None and backward == None: return None

		
