class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	def isEmpty(self):
		return len(self.queue) == 0

	def insert(self, data,priority):
		self.queue.append([data,priority])

	# for popping an element based on Priority
	def pop(self):
		try:
			max_val = 0
			for i in range(len(self.queue)):
			    if self.queue[i][1] > self.queue[max_val][1]:
				    max_val = i
			item = self.queue[max_val][1]
			del self.queue[max_val]
			return item
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
	myQueue = PriorityQueue()
	myQueue.insert("Task1",12)
	myQueue.insert("Task2",1)
	myQueue.insert("Task3",14)
	myQueue.insert("Task4",7)
	print(myQueue)		
	while not myQueue.isEmpty():
		print(myQueue.pop())