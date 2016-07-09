import re

class Address:
	def __init__(self, street, city, state, zipCode):
		self.street = street
		self.city = city
		self.state = state
		self.zipCode = zipCode

	def getStreet(self):
		return self.street

	def getCity(self):
		return self.city

	def getState(self):
		return self.state

	def getZip(self):
		return self.zipCode

	def formatOutput(self):
		return self.street + '\t' + self.city + '\t' + self.state + '\t' + self.zipCode

	def normalize(self):
		self.toUpper()
		self.removePunctuation()
		self.stripLeadingTrailingSpace()
		self.streetPrefix()
		self.streetSuffixAbbr()
		self.stateAbbr()

	def toUpper(self):	
		self.street = self.street.upper()
		self.city = self.city.upper()
		self.state = self.state.upper()
		self.zipCode = self.zipCode.upper()

	def isCompleteAddress(self):
		if (self.street == "" or self.city == "" or self.state == "" or self.zipCode == ""):
			return False
		else:
			return True	

	def stripLeadingTrailingSpace(self):
		self.street = self.street.strip()
		self.city = self.city.strip()
		self.state = self.state.strip()
		self.zipCode = self.zipCode.strip()

	def removePunctuation(self):
		punctuation = '[!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~]'
		self.street = re.sub(punctuation, "", self.street)
		self.city = re.sub(punctuation, "", self.city)
		self.state = re.sub(punctuation, "", self.state)
		self.zipCode = re.sub(punctuation, "", self.zipCode)

	def streetPrefix(self):
		self.street = re.sub(r'(WEST)( [A-Z]+ [A-Z]+)$', r'W\2', self.street)
		self.street = re.sub(r'(NORTH)( [A-Z]+ [A-Z]+)$', r'N\2', self.street)
		self.street = re.sub(r'(EAST)( [A-Z]+ [A-Z]+)$', r'E\2', self.street)
		self.street = re.sub(r'(SOUTH)( [A-Z]+ [A-Z]+)$', r'S\2', self.street)
		self.street = re.sub(r'(NORTHWEST)( [A-Z]+ [A-Z]+)$', r'NW\2', self.street)
		self.street = re.sub(r'(NORTHEAST)( [A-Z]+ [A-Z]+)$', r'NE\2', self.street)
		self.street = re.sub(r'(SOUTHEAST)( [A-Z]+ [A-Z]+)$', r'SE\2', self.street)
		self.street = re.sub(r'(SOUTHWEST)( [A-Z]+ [A-Z]+)$', r'SW\2', self.street)
		self.street = re.sub(r' NORTH$', r' N', self.street)
		self.street = re.sub(r' EAST$', r' E', self.street)
		self.street = re.sub(r' SOUTH$', r' S', self.street)
		self.street = re.sub(r' WEST$', r' W', self.street)
		self.street = re.sub(r' NORTHWEST$', r' NW', self.street)
		self.street = re.sub(r' NORTHEAST$', r' NE', self.street)
		self.street = re.sub(r' SOUTHEAST$', r' SE', self.street)
		self.street = re.sub(r' SOUTHWEST$', r' SW', self.street)

	def getAbbrevs(self, file):
		addressFile = open(file, 'r')
		abbrevs = {}
		for line in addressFile:
			data = line.split('\t')
			abbrevs[data[0]] = data[1].replace('\n', "")
		addressFile.close()
		return abbrevs

	def streetSuffixAbbr(self):
		abbrevs = self.getAbbrevs("suffixAbbreviations.txt")
		for suffix, abbreviation in abbrevs.items():
			replace = r"( " + suffix + r")( )*(NE|NW|SE|SW|N|S|E|W)*$"
			replaceWith = r" " + abbreviation + r"\2\3"
			self.street = re.sub(replace, replaceWith, self.street)

	def stateAbbr(self):
		abbrevs = self.getAbbrevs("stateAbbreviations.txt")
		for state, abbreviation in abbrevs.items():
			self.state = self.state.replace(state, abbreviation)
