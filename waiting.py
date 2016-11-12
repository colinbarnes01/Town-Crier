class Waiting(BotState):

	def changeState(context):
		context.setState( Ready() )