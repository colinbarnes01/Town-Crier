from state import BotState
import ready
import time

class Waiting(BotState):

	def startTimer(self):
		time.sleep(300)
		self.changeState(self.context)

	def changeState(self):
		self.context.setState( ready.Ready(self.context) )



