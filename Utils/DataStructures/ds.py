class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self, head=None, l=None):
    self.head = head

    if l is not None:
      self.head = Node(l[0])
      current_node = self.head
      for i in range(len(l)):
        if i == 0:
          continue

        current_node.next = Node(l[i])
        if i == len(l):
          current_node.next = None

        else:
          current_node = current_node.next

    def __repr__(self):
      current_node = self.head
      nodes = []
      while current_node is not None:
        nodes.append(str(current_node.value))
        current_node = current_node.next

      nodes.append('None')
      return ' -> '.join(nodes)

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def __len__(self):
    count = 0
    current_node = self.head
    while current_node is not None:
      count += 1
      current_node = current_node.next
    
    return count

  def __getitem__(self, item):
    current = self.head
    count = 0

    if type(item) is int:  
      while count != item:
        current = current.next
        count += 1
      return current.value, current

    elif type(item) is str:
      while current.value != item:      
        current = current.next
        count +=1
      return count, current

    else:
      return None