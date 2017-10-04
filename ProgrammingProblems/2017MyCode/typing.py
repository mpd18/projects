def areSimiliar(string1,string2,keyboard):
	counter = 0
	for x in range(0,len(string1)):
		if(string2[x] in keyboard[string1[x]] or string2[x] == string1[x]):	
			counter+=1
	if(counter == len(string1)):
		return 2
	return 3


keyboard = {"a" : "bkj", "b" : "ajklc", "c" : "bklmd",
			"d" : "clmne", "e" : "dmnof", "f" : "enopg",
			"g" : "fopqh", "h" : "gpqri","i":"hqr",
			"j":"abkts","k":"abclutsj","l":"bdcmvutk",
			"m":"cdenwvul","n":"defoxwvm","o":"efgpyxwn",
			"p":"fghqzyxo","q":"ghirzyp","r":"zqhi",
			"s":"jkt","t":"sjklu","u":"tklmv","v":"ulmnw",
			"w":"vmnox","x":"wnopy","y":"xopqz","z":"ypqr"}
		
list = []
with open("../2017/typing.in","r") as f:
	for line in f:
		list.append(line.rstrip().split())
		

number = int(list[0][0])

for i in range(1,number+1):
	if(list[i][0] == list[i][1]):
		print("1")
	elif(len(list[i][0]) != len(list[i][1])):
		print("3")
	else:
		print(areSimiliar(list[i][0],list[i][1],keyboard))
