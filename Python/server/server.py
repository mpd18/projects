'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 56789 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
	#Sending message to connected client
	conn.send('Welcome to the calculator. Please enter in an equation type in 0/0 to break\n') #send only takes string
	
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		 
		#Receiving from client
		data = conn.recv(1024)
		data = str(data.rstrip())
		if data == "0/0":
			conn.sendall("OK Bye Bye\n")
			conn.close()
			break
		else:
			if ' ' in data:
				#conn.sendall("= " + data + "\n")
				data = data.split()
				data = str.join('',data)
				postfix = toPostfix(data)
				result = str(evaluatePostfix(postfix))
				conn.sendall("= " + result + "\n")
			else:
				postfix = toPostfix(data)
				result = str(evaluatePostfix(postfix))
				conn.sendall("= " + result + "\n")
		  
	#came out of loop
	conn.close()

#yay I wrote my own postfix evaluator
def toPostfix(equation):
	opStack = []
	postfix = ''
	# for length of the equation
	x=0
	while x < len(equation):
		precedance = returnPrecedance(equation[x])
		if precedance < 0:
			while x < len(equation) and returnPrecedance(equation[x]) < 0:
				postfix += equation[x]
				x+=1
			postfix += " "
			continue
		elif equation[x] == '(':
			opStack.append(['(',0])
		elif equation[x] == ')':
			for i in range(len(opStack)-1,0,-1):
				if opStack[i][0] == '(':
					operator = opStack.pop()
					break
				else:
					operator = opStack.pop()
					postfix += operator[0] + " "
					
		elif len(opStack) == 0 or opStack[len(opStack) - 1][1] < precedance:
			opStack.append([equation[x],precedance])
		elif opStack[len(opStack) - 1][1] > precedance:
			for y in range(len(opStack)-1,0,-1):
				if opStack[y][1] >= precedance:
					operator = opStack.pop()
					postfix += operator[0] + " "
				else:
					break
			opStack.append([equation[x],precedance])
		x+=1
					
	for x in range(0,len(opStack)):
		operator = opStack.pop()
		postfix += operator[0] + " "
	return postfix

def evaluatePostfix(postfix):
	postfix = postfix.split()
	stack = []
	for i in range(0,len(postfix)):
		if postfix[i] == "+":
			a = float(stack.pop())
			b = float(stack.pop())
			result = b+a
			stack.append(result)
		elif postfix[i] == '-':
			a = float(stack.pop())
			b = float(stack.pop())
			result = b-a
			stack.append(result)
		elif postfix[i] == '*':
			a = float(stack.pop())
			b = float(stack.pop())
			result = b*a
			stack.append(result)
		elif postfix[i] == '/':
			a = float(stack.pop())
			b = float(stack.pop())
			result = b/a
			stack.append(result)
		elif postfix[i] == '^':
			a = float(stack.pop())
			b = float(stack.pop())
			result = b**a
			stack.append(result)
		else:
			stack.append(float(postfix[i]))
	return stack[0]
			
		
def returnPrecedance(operand):
	if operand == '+':
		return 1
	if operand == '-':
		return 1
	if operand == '*':
		return 2
	if operand == '/':
		return 2
	if operand == '^':
		return 3
	if operand == '(':
		return 20
	if operand == ')':
		return 20
	else:
		return -1
	
 
#now keep talking with the client
while 1:
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))

s.close()