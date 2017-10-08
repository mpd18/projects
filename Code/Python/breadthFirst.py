class Queue:
	def __init__(self):
		self.queue = []
		self.length = 0
		self.head = 0
	
	def enqueue(self,element):
		self.queue.append(element)
		self.length +=1
		return True
		
	def dequeue(self):
		self.length -=1
		self.head +=1
		return self.queue.popleft()
		
	def isEmpty(self):
		if(self.length==0):
			return true;
		return False
	def first(self):
		return self.queue[self.head]

class Search:
		
	def getMatrixFromFile(self,file):
		matrix = []
		with open(file) as f:
			for line in f:
				splitline = line.rstrip().split()
				matrix.append(list(map(int,splitline)))
		return matrix
	
	def breadthFirst(self,first):
		queue =Queue()
		visited = []
		self.breadthFirstRec(visited,queue,first)
		
		
	def breadthFirstRec(self,visited,queue,current):
		print(current)
		queue.enqueue(current)
		visited.
		if(not queue.isEmpty()):
			for node in self.matrix[queue.first()]:
				if(not visited[node]):
					queue.enqueue(node)
			breadthFirstRec(self,visited,queue,current)
		
		
	def printMatrix(self):
		for row in self.matrix:
			print(row)
		return None
		
	def __init__(self,file):
		self.matrix = self.getMatrixFromFile(file)
		
		
		
search = Search("list1.txt")
search.printMatrix()
search.breadthFirst(0);
	