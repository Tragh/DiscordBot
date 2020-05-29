class BotAction:
	channels=[]
	command=None
	def action(message):
		pass
		
class BotActionController:
	def __init__(self):
		self.botActionsList=[]
	def createBotAction(self):
		return BotActionFactory(self)

class BotActionFactory:
	def __init__(self,parent):
		self.botAction=BotAction()
		self.parent=parent
	def onCommand(self, command):
		self.botAction.command=command
		return self
	def inChannel(self,channel):
		if channel not in self.botAction.channels:
			self.botAction.channels.append(channel)
		return self
	def takeAction(self,action):
		self.botAction.action=action
		return self
	def done(self):
		self.parent.botActionsList.append(self.botAction)
