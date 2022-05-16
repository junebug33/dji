from djitellopy import Tello

tello = Tello()

tello.connect()

'''
Asks the user over and over how far they would like to fly & which direction
Executes the command based off of user input
Thats it!
'''

while True:
	try:
		d = input('How far (cm) would you like it to fly? (default = 20cm)\n-> ')

		try: distance = d if len(d) and int(d) else 20
		except ValueError:
			print('Please enter an integer!\n')
			continue

		match input('W - Forward\nA - Left\nS - Backward\nD - Right\nI - Upwards\nK - Downwards\nC - Clockwise\nV - Counterclockwise\nL - Land\nT - Takeoff\nS - STOP\n-> ').lower():
			case 'w':
				tello.move_forward(distance)
			case 'a':
				tello.move_left(distance)
			case 's':
				tello.move_back(distance)
			case 'd':
				tello.move_right(distance)
			case 'i':
				tello.move_up(distance)
			case 'k':
				tello.move_down(distance)
			case 'c':
				tello.rotate_clockwise(distance)
			case 'v':
				tello.rotate_counter_clockwise(distance)
			case 'l':
				tello.land()
			case 't':
				tello.takeoff()
			case 's':
				tello.emergency()
	except KeyboardInterrupt: break
