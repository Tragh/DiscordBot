class BotAction:
	def __init__(self, *, channelList, onCommand=None, takeAction):
		self.channels=channelList
		self.command=onCommand
		self.action=takeAction
		
class BotActionController:
	def __init__(self):
		self.botActionsList=[]
	def addBotAction(self, *, channelList, onCommand=None, takeAction):
		self.botActionsList.append(BotAction(channelList=channelList, onCommand=onCommand, takeAction=takeAction))

