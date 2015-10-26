''' Implementing binary search tree in Python 

    Following Operations are included -
    1) Inorder Traversal
    2) Preorder Traversal
    3) Postorder Traversal
    4) Add a node
    5) Delete a node'''

class tree:
  def __init__(self, value = 0):  # Similar to constructor
    self.val = value
    self.left = None
    self.right = None

  def inorder(self):
    if self.left:
      self.left.inorder()
    print self.val
    if self.right:
      self.right.inorder()
    return

  def preorder(self):
    print self.val
    if self.left:
      self.left.preorder()
    if self.right:
      self.right.preorder()
    return

  def postorder(self):
    if self.left:
      self.left.postorder()
    if self.right:
      self.right.postorder()
    print self.val
    return

  def add_node(self , element):    # Recursive function to reach bottom of tree for addition
    if self.val == element:
      return
    elif  element > self.val:
      if self.right:
        self.right.add_node(element)
      else:
        self.right = tree(element)

    else:
      if self.left:
        self.left.add_node(element)
      else:
        self.left = tree(element)

  def remove_node(self,element):   # Remove a particular element from tree
    if self.val>element:
      self.left = self.left.remove_node(element)

    elif self.val<element:
      self.right = self.right.remove_node(element)
     
    else:                          # Actual delete operation from here
      if self.left == None:
        return self.right
      elif self.right == None:
        return self.left
      else:                        # In case node has two children (Sucessor element of node replaces it)
        self.val = self.getRight()
        self.right = self.right.remove_node(self.val)
        return self
    return self

  def getRight(self):              # Function to get the closest large element of an node
    current = self.right
    while current.left != None:
      current = current.left
    return current.val

def populate():                    # Function to initially populate data
  a = tree(10)
  a.left = tree(7)
  a.right = tree(12)
  a.left.left = tree(4)
  a.left.right = tree(8)
  a.right.left = tree(11)
  a.right.right = tree(14)
  return a


def main():
  Tree = populate()
  print 'Inorder Traversal'
  Tree.inorder()
  print 'Post-Order Traversal'
  Tree.postorder()
  print 'Pre-Order Traversal'
  Tree.preorder()
  Tree.add_node(5)
  Tree.add_node(9)
  print 'New preorder Traversal'
  Tree.preorder()
  Tree.remove_node(7)
  print 'After delete Inorder Traversal'
  Tree.inorder()

main()
