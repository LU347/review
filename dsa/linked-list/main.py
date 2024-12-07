
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtStart(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    else:
      new_node.next = self.head
      self.head = new_node

  def insertAtIndex(self, data, index):
    if (index == 0):
      self.insertAtStart(data)
      return

    position = 0
    current_node = self.head
    while (current_node != None and position+1 != index):
      position = position + 1
      current_node = current_node.next
    
    if current_node != None:
      new_node = Node(data)
      new_node.next = current_node.next
      current_node.next = new_node
    else:
      print("Index not present")

  def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    current_node = self.head
    while(current_node.next):
      current_node = current_node.next

    current_node.next = new_node

  def updateNode(self, val, index):
    current_node = self.head
    position = 0
    if position == index:
      current_node.data = val
    else:
      while(current_node != None and position != index):
        position = position + 1
        current_node = current_node.next
        
        if current_node != None:
          current_node.data = val
        else:
          print("Index not present")

  def printLL(self):
    current_node = self.head
    while(current_node):
      print(current_node.data)
      current_node = current_node.next
