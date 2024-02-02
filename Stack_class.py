"""
CISC-121 2023W
Name: <Anneth Sivakumar>
Student Number: <20320973>
Email: <21as221@queensu.ca>
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""

class Stack:
  """
  -------------------------------------------------------
  A class representing a Stack.
  -------------------------------------------------------
  """

  def __init__(self):
    """
    -------------------------------------------------------
    Initializes an empty stack. Data is stored in a Python list.
    Use: stack = Stack()
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        a new Stack object (Stack).
    -------------------------------------------------------
    """
    self.items = []

  def is_empty(self):
    """
    -------------------------------------------------------
    Determines if the stack is empty.
    Use: b = stack.is_empty()
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        True if stack is empty, False otherwise.
    -------------------------------------------------------
    """
    return self.items == []

  def push(self, value):
    """
    -------------------------------------------------------
    Pushes a copy of value onto the top of the stack.
    Use: stack.push(value)
    -------------------------------------------------------
    Parameters:
        value - value to be added to stack.
    Returns:
        None
    -------------------------------------------------------
    """
    self.items.append(value)

  def pop(self):
    """
    -------------------------------------------------------
    Pops and returns the top of stack. The value is removed
    from the stack. Attempting to pop from an empty stack
    throws an exception.
    Use: value = stack.pop()
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        value - the value at the top of stack.
    -------------------------------------------------------
    """
    if len(self.items) == 0:
      print("Can't Pop On Empty Stack")
    else:
      return self.items.pop()

  def peek(self):
    """
    -------------------------------------------------------
    Returns a copy of the value at the top of the stack.
    Attempting to peek at an empty stack throws an exception.
    Use: value = stack.peek()
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        value - a copy of the value at the top of stack.
    -------------------------------------------------------
    """
    if len(self.items) == 0:
      return "Can't Peek On Empty Stack!"
    else:
      return self.items[-1]

  def size(self):
    """
    -------------------------------------------------------
    Returns the number of items in the stack.
    Use: n = stack.size()
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        The number of items in the stack (int).
    -------------------------------------------------------
    """
    return len(self.items)

  def reverse(self):
    """
    -------------------------------------------------------
    Reverses the contents of the source stack.
    Use: source.reverse()
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        None.
    -------------------------------------------------------
    """
    self.items.reverse()

  def __str__(self):
    """
    -------------------------------------------------------
    Prints the contents of the stack
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        The list of elements present in the stack.
    -------------------------------------------------------
    """
    return str(self.items)
