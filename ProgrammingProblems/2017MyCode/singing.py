def numberOfClicks(songs,numToPlay,second):
	clickCounter = 0;
	last = second[0]
	for i in second[1:]:
		next = int(i)
		if(last==next):
			clickCounter +=1
		elif(next > last):
			#min of clicks forward or clicks back
			clickCounter += min(next-last -1,last+1 + songs-next)
		elif(next < last):
			clickCounter += min((songs-last -1) + next,last-next +1)
		last = next
	return clickCounter

with open("../2017/singing.in","r") as f:
	number = int(f.readline().rstrip())
	for x in range (0,number):
		first = []
		second = []
		#songs and how many she wants to hear
		first = f.readline().rstrip().split()
		first = list(map(int,first))
		#list of songs in order
		second = f.readline().rstrip().split()
		second = list(map(int,second))
		print(numberOfClicks(first[0],first[1],second))