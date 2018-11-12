import numpy
import cv2
import GPIO


# Define motor class
class DCmotor:
	def __init__(self,PWMPin,DirPin,EncoderPins,MotorType,LimitPins):
		# set pins
		self.pwm = PWMPin  # int corresponding to the GPIO pin connected to PWM port on driver board
		self.dir = DirPin  # int corresponding to GPIO pin connected to direction port on driver
		self.type = MotorType  # int, 0 is a arm motor, 1 is the leg motor
		self.limits = LimitPins  # GPIO pins monitoring the limit switches
		if notempty(EncoderPins):
			# if a two element list of integers is provided setup the encoder pins (arm motor)
			self.encoder = EncoderPins
		# also define key vars
		self.position = 57
		self.velocity = 57
		# default gains from matlab pid tuner
		self.kp = .705
		self.ki = 5.38
		self.kd = .0013
		return none

	def setGains(self,newGains):
		self.kp = newGains[0]
		self.ki = newGains[1]
		self.kd = newGains[2]
		return none

	def getGains(self)
		myGains = [0,0,0]
		myGains[0] = self.kp
		myGains[1] = self.ki
		myGains[2] = self.kd
		return myGains

	def getPosition(self):
		return self.position

	def getVelocity(self):
		return self.velocity

	def setPosition(self,DesPosition)
		# add servo position functionality
		finished = False
		Eint = 0.0
		recentPos = [-10.0,-10.0,-10.0,-10.0,-10.0,-10.0,-10.0,-10.0,-10.0,-10.0]
		while(not(finished)):
			posE = DesPosition - self.position
			Eint = Eint + posE
			DF = posE*self.kp + Eint*self.ki + self.velocity*self.kd
			self.setOpenLoop(DF)


		return none

	def setOpenLoop(self,DutyFactor):
		GPIO.pwm(self.PWMPin,Dutyfactor)
		return none

	def readEncoder(self)
		if defined(self.encoder):

		else:
			return none
		return encoderdata

	def zeroLimitState(self):
		state = false
		if(GPIO.read(self.limits(0)) == True):
			state = True
		return state

	def setZero(self):
		while(self.zeroLimitState() == false):
			self.setOpenLoop(.1)
		self.position = 0
		return none




def startup():
	# Initilaize vision system and zero the motors

	# instantiate the motors
	DCmotor(Glove,11,11,[11,11],0,[11,11])
	DCmotor(Blocker,11,11,[11,11],0,[11,11])
	DCmotor(Pads,11,11,[],1,[11,11])

	#zero the motors
	Glove.setZero()
	Blocker.setZero()
	Pads.setZero()

