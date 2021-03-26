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

def rx(interfaces: list, in_mean_time, in_sd_time):
	
	while True:
		time.sleep(abs(random.gauss(in_mean_time, in_sd_time)))
		
		frame_id = hex(abs(random.randint(100, 5000)))
		frame_time = time.ctime(time.time())
		input_int, output_int = random.sample(interfaces, 2)

		queue.enqueue(Node(value=(frame_id, frame_time, input_int, output_int)))		

def tx(out_mean_time, out_sd_time):
	while True:
		time.sleep(abs(random.gauss(out_mean_time, out_sd_time)))
		queue.dequeue()

	

def app():
	# List of interfaces to simulate
	interfaces = range(1,21)

	# Input/output mean and standard deviation for randomly time
	# to await for rx/tx
	in_mean_time, in_sd_time = (3,2)
	out_mean_time, out_sd_time = (3,2)

	# Create threads
	rx_thread = threading.Thread(target=rx, args=(interfaces, in_mean_time, in_sd_time))
	tx_thread = threading.Thread(target=tx, args=(out_mean_time, out_sd_time))

	rx_thread.start()
	tx_thread.start()

	refresh_time = 0.5

	# Will refresh the queue table in a rate of 'refresh_time' value
	while True:
		time.sleep(refresh_time)
		os.system('clear') if os.name == 'posix' else os.system('cls')
		
		print('Network Equipment Interfaces Queue')
		print(queue, end= '\r')
