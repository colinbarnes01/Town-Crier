from state import BotState
import ready
import time

class Waiting(BotState):

	status = "WAITING"

	def changeState(self):
		self.context.setState( ready.Ready(self.context) )



