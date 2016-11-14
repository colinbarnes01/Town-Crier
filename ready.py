from state import BotState
import waiting

class Ready(BotState):

	def changeState(self, context):
		context.setState( waiting.Waiting() )