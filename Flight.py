from Travel import Travel
from random import uniform

class Flight(Travel):
	def __init__(self):
		print "Start!"
	def __str__(self):
		return ''
		
	def go(self):
		while (not self.flag == 'y' and self.flag1 =='y'):
			Flight.simulator_reply('The angle is:')
			angle = uniform(-90,90)
			Flight.simulator_reply('%.2f' % angle)
			flag1 = self.user_action('Should we correct it? (y/n)')
			if (flag1 == 'n'):
				Flight.simulator_reply('We crashed!')
				break
			Flight.simulator_reply('We corrected wings with:','\n', '%.2f' % -angle)
			
			flag = self.user_action('Should we stop? (y/n)')	
			
	def user_action(self, message):
		return raw_input(message)
