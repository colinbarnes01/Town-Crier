from state import State
import waiting

class Ready(State):
	
	status = "READY"

	def changeState(self):
		self.context.setState( waiting.Waiting(self.context) )
