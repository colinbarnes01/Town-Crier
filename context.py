
import ready

class Context:

	def __init__(self):
		from state import State
		self.currentState = ready.Ready(self)

	def setState(self, state):
		self.currentState = state


	def changeState(self):
		self.currentState.changeState()