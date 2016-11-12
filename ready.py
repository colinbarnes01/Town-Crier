class Ready(BotState):

	def changeState(context):
		context.setState( Waiting() )