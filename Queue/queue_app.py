from prettytable import PrettyTable
import time
import threading
import random
from Utils.DataStructures.ds import Node, Queue
import os


class TrafficQueue(Queue):
	"""
	A class used to represent a Traffic Queue, this class inherits from
	the class Queue.

	...

	Attributes
	----------
	head : Node or None, Optional
		The reference value for the head node.
	l : List or None, Optional
		List object to convert to Queue.
"""
	def __init__(self, head=None, l=None):
		super().__init__(head=None, l=None)

		self.frame_table = PrettyTable()
		self.frame_table.field_names = ['Order', 'Id', 'Time', 'In Interface','Out Interface']
	
		# If a list was passed create a linked list upon that list
		if l is not None:
			self.list_to_linked(l)


	def __repr__(self):
		self.frame_table.clear_rows()
		if self.front:
			count = 0
			for node in self:
				count += 1
				frame_id, frame_time, input_int, output_int = node.value
				self.frame_table.add_row([count, frame_id, frame_time, input_int, output_int])

		return self.frame_table.get_string()

queue = TrafficQueue()

def rx():
	interfaces = range(1,21)
	while True:
		time.sleep(abs(random.gauss(3, 2)))
		
		frame_id = hex(abs(random.randint(100, 5000)))
		frame_time = time.ctime(time.time())
		input_int, output_int = random.sample(interfaces, 2)

		queue.enqueue(Node(value=(frame_id, frame_time, input_int, output_int)))		

def tx():
	while True:
		time.sleep(abs(random.gauss(3, 2)))
		queue.dequeue()

	

def app():
	rx_thread = threading.Thread(target=rx)
	tx_thread = threading.Thread(target=tx)

	rx_thread.start()
	tx_thread.start()

	while True:
		time.sleep(0.5)
		os.system('clear') if os.name == 'posix' else os.system('cls')
		
		print('Network Equipment Interfaces Queue')
		print(queue.__repr__(), end= '\r')


		
		
		
	

	
	