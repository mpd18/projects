lineArray = []
with open("../2017/energy.in") as inFile:
	for line in inFile:
		lineArray.append(line.rstrip());
lineArray[0] = lineArray[0].split();

first = int(lineArray[0][0]);
next = int(lineArray[0][1]);
number = int(lineArray[1]);
for i in range (2,number+2):
	if(int(lineArray[i]) < 1000):
		print(lineArray[i] + " " + str(int(lineArray[i]) * first))
	else:
		money += 1000*first
		money += (int(lineArray[i]) - 1000)*next
		print(lineArray[i] + " " + str(money))
	money = 0