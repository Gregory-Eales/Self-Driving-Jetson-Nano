from inputs import get_gamepad
import time

class JoystickController(object):

	def __init__(object):

		self.moves = ["BTN_EAST", "BTN_WEST",
			 "BTN_NORTH", "BTN_SOUTH"]

t = time.time()

def timer(t, length):

	if (time.time()-t)<length:
		return True
	else: return False

max_event = 0
event_types = []


while timer(t, 30):
	events = get_gamepad()
	#print(time.time()-t)
	for event in events:

		if event.ev_type not in event_types:
			event_types.append(event.ev_type)
		if event.state > max_event: max_event = event.state

		if event.ev_type == "Key":
			print(event.ev_type, event.code, event.state)
			# print("max_state:", max_event)


print(event_types)
