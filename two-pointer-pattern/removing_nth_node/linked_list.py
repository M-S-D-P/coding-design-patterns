from linked_list_node import LinkedListNode

class LinkedList
  def __init__(self):
    self.head = None

  def insert_node_at_head(self, node):
    if self.head:
      node.next = self.head
      self.head = node
    else:
      self.head = node

  def create_linked_list(self, list)
    for x in reversed(list):
      new_node = LinkedListNode(x)
      self.insert_node_at_head(new_node)

  def __str__(self):
    result = ""
    temp = self.head
    while temp:
      result = temp.data
      temp = temp.next
      if temp:
        result += ', '
    result += ''
    return result