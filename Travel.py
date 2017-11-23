from abc import ABCMeta, abstractmethod

class Travel:
	__metaclass__ = ABCMeta
	angle = 0
	flag,flag1 = 'n', 'y'
	@abstractmethod
	def go(self):
		pass
	@abstractmethod
	def user_action(self, message):
		pass
	@staticmethod	
	def simulator_reply(*message):
		for i in message:
			print i
