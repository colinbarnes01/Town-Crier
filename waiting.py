from state import State
import ready


class Waiting(State):

	status = "WAITING"

	def changeState(self):
		self.context.setState( ready.Ready(self.context) )



