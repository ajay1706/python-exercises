class CLub:
	def __init__(self,name):
		self.name = name
		self.players = []
	def __len__(self):
		return len(self.players)
	def __getitem__(self,i):
		return self.players[i]
	def __repr__(self):
		return 'Club {}:{}'.format(self.name,self.players)
	def __str__(self):
		return 'Club {} with {} players'.format(self.name, len(self))

