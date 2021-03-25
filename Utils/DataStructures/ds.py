class Node:
	"""
	A class used to represent a Node

	...

	Attributes
	----------
	value : Object
		The reference value for the node 
	next : Object
		The next node wich the current one points to
"""
	def __init__(self, value=None, next=None):
		"""
	Parameters
	----------
	value: Object, optional 
		The value to instancing the Node.
	Next: Object, optional
		Next Node to point. By default it will be None.
	"""
		self.value = value
		self.next = next


class LinkedList:
	"""
	A class used to represent a Linked List.

	...

	Attributes
	----------
	head : Node or None, Optional
		The reference value for the head node.
	l : List or None, Optional
		List object to convert to Linked List.
"""
	def __init__(self, head=None, l=None):

		# Points to head
		self.head = head

		# If a list was passed create a linked list upon that list
		if l is not None:
			self.list_to_linked(l)
			

	def list_to_linked(self, lst: list, reverse:bool=False):
			# Set the head to point to the first node
			self.head = Node(lst[0])
			current_node = self.head
			list_len = len(lst)
			# Iterates over the list and check for the position of the current element in the list.
			# If the current is the last element, points it to None, else update the current to the next one.
			for i in range(1, list_len):
				current_node.next = Node(lst[i])

				if i == list_len:
					current_node.next = None

				else:
					current_node = current_node.next



	def __repr__(self):
		current_node = self.head
		nodes = []

		# Append all nodes to a normal list and join the list with '->' characters.
		while current_node is not None:
			nodes.append(str(current_node.value))
			current_node = current_node.next

		nodes.append('None')
		return ' -> '.join(nodes)

	# Magic method for traversing the Linked List
	# This method is called while iterating the Linked List
	def __iter__(self):
		node = self.head
		# Jumps into every node and returns it each time that is required throw the iteration, while is not None
		while node is not None:
			yield node
			node = node.next

	# Magic method that returns the length of the Linked List
	def __len__(self):
		count = 0

		# Iterates over the list and count in every iteration
		for node in self:
			count += 1

		return count

	# Magic method for returning a tuple with the value of the node, and the Node given an index at the input
	def __getitem__(self, idx: int):
		current = self.head
		count = 0

		# Returns current node given the index at input
		while count != idx:
			current = current.next
			count += 1
		return current

	# Insert a node at the end
	def append(self, item: Node):
		#If there's not node in Linked List, set item to the head
		if self.head is None:
			self.head = item
			self.head.next = None
			return None

		# Look for the last node and points the next node to the item
		for node in self:
			if node.next is None:
				node.next = item
				item.next = None

	# Insert at the begining of the list
	def insert_first(self, item: Node):
		# Set the current head as the new item next node
		item.next = self.head
		# Set the new item as new head
		self.head = item

class Queue(LinkedList):
	"""
	A class used to represent a Queue, this class inherits from
	the class Linked List.

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
	
		# If a list was passed create a linked list upon that list
		if l is not None:
			self.list_to_linked(l)

	@property
	def front(self):
		return self.head

	@front.setter
	def front(self, new: Node):
		self.head = new
		
	def enqueue(self, equeueing: Node):
		# Calls the inherited method 'append', wich iterates
		# over the list and add the node after the last one. 
		self.append(equeueing)

	def dequeue(self):
		# Deteches the actual front and points to the next one.
		dequeued = self.front
		self.front = self.front.next
		dequeued.next = None

		return dequeued

class Stack(LinkedList):
	def __init__(self, head=None, l=None):
		super().__init__(head=None, l=None)

		# If a list was passed create a linked list upon that list
		if l is not None:
			self.list_to_linked(lst=l[::-1])

	@property
	def top(self):
		return self.head

	@top.setter
	def top(self, new: Node):
		self.head = new

	def push(self, item: Node):
		old_top = self.top
		self.top = item
		self.top.next = old_top
		
	def pop(self):
		popped = self.top
		self.top = self.top.next
		popped.next = None

		return popped