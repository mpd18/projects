#this def is mostly pseudocode
def replace(inString,replaceArray):
	splitString = String.split(inString)
	for word in splitString:
		if(word in replaceArray):
			word = replaceArray
	return String.join(splitString);
