from state import BotState
import ready

class Waiting(BotState):

	def changeState(self, context):
		context.setState( ready.Ready() )