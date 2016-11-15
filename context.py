import ready

class BotContext:

	def __init__(self):
		self.currentState = ready.Ready(self)

	def setState(self, state):
		self.currentState = state

	def changeState(self):
		self.currentState.changeState()