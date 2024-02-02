"""
CISC-121 2023W
Name: <Anneth Sivakumar>
Student Number: <20320973>
Email: <21as221@queensu.ca>
Date: 2023-03-29

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
from Stack_class import Stack

def main():
  """
  This function implements the interface for the program.
  Parameters: 
      None.
  Return: 
      None.
  """
  # Initiate Stack.
  s = Stack()
  
  # Push some values onto the stack.
  s.push(10)
  s.push(20)
  s.push(30)
  s.push(40)
  s.push(50)
  s.push(60)
  s.push(70)
  s.push(80)
  s.push(90)
  s.push('A')
  s.push('b')
  print(f"Original Stack: {s}" + "\n")

  # Pop some values off the stack and test size function.
  s.pop()
  print(f"Stack After Pop: {s}")
  print(f"Size of Stack: {s.size()}" + "\n")
  #s.pop()
  #print(f"Stack After Pop: {s}")
  #print(f"Size of Stack: {s.size()}" + "\n")
  #s.pop()
  #print(f"Stack After Pop: {s}")
  #print(f"Size of Stack: {s.size()}" + "\n")
  #s.pop()
  #print(f"Stack After Pop: {s}")
  #print(f"Size of Stack: {s.size()}" + "\n")

  # Test peek function after each pop.
  print(f"Stack: {s}")
  print(f"Peek: {s.peek()}")
  print(f"Stack: {s}" + "\n")
  #s.pop()
  #print(f"Stack: {s}")
  #print(f"Peek: {s.peek()}")
  #print(f"Stack: {s}" + "\n")
  #s.pop()
  #print(f"Stack: {s}")
  #print(f"Peek: {s.peek()}")
  #print(f"Stack: {s}" + "\n")
  #s.pop()
  #print(f"Stack: {s}")
  #print(f"Peek: {s.peek()}")
  #print(f"Stack: {s}" + "\n")

  # Test is_empty function.
  print(f"Stack: {s}")
  print(f"Is Stack Empty: {s.is_empty()}" + "\n")
  s.pop()
  s.pop()
  s.pop()
  print(f"Stack: {s}")
  print(f"Is Stack Empty: {s.is_empty()}" + "\n")
  #s.pop()
  #s.pop()
  #s.pop()
  #s.pop()
  #s.pop()
  #s.pop()
  #s.pop()
  #s.pop()
  #print(f"Peak: {s.peek()}")
  #print(f"Stack: {s}")
  #print(f"Is Stack Empty: {s.is_empty()}" + "\n")

  # Test reverse stack function.
  print(f"Normal Stack: {s}")
  s.reverse()
  print(f"Reverse Stack: {s}" + "\n")
  s.pop()
  s.pop()
  print(f"Normal Stack: {s}")
  s.reverse()
  print(f"Reverse Stack: {s}" + "\n")
  s.pop()
  s.pop()
  print(f"Normal Stack: {s}")
  s.reverse()
  print(f"Reverse Stack: {s}" + "\n")


main()