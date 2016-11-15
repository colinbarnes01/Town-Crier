from state import BotState
import waiting

class Ready(BotState):

	def changeState(self):
		self.context.setState( waiting.Waiting(self.context) )