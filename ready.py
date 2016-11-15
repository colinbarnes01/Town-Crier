from state import BotState
import waiting

class Ready(BotState):
	
	status = "READY"

	def changeState(self):
		self.context.setState( waiting.Waiting(self.context) )
