"""
CISC-121 2023W
Name:  <Anneth Sivakumar>
Student Number: <20320973>
Email: <21as221@queensu.ca>
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
from hotel_classes import *
from datetime import *

def main():
  """
  This function implements the interface for the program.
  Parameters: 
      None.
  Return:
      None.
  """
  # Creating instances of each type of room.
  suite1 = Suite(101, True, datetime(2023,4,3))
  suite2 = Suite(102, False, datetime(2023, 4, 28))
  suite3 = Suite(103, True, datetime(2023, 4, 21))
  suite4 = Suite(104, True, 2023-4-21)
  standard1 = StandardRoom(201, True, datetime(2023, 3, 28))
  standard2 = StandardRoom(201, False, datetime(2023, 3, 29))
  standard3 = StandardRoom(201, True, 2023-4-21)
  standard4 = StandardRoom(201, True, datetime(2023, 3, 30))
  taylorsuite1 = TaylorSuite(301, True, datetime(2023, 3, 28))
  taylorsuite2 = TaylorSuite(302, False, datetime(2023, 3, 28))
  taylorsuite3 = TaylorSuite(303, True, datetime(2023, 3, 28))
  taylorsuite4 = TaylorSuite(304, False, datetime(2023, 3, 28))
  taylorsuite5 = TaylorSuite(305, True, datetime(2023, 3, 28))
  taylorsuite6 = TaylorSuite(306, True, datetime(2023, 3, 28))
  taylorsuite7 = TaylorSuite(307, True, datetime(2023, 3, 28))
  taylorsuite8 = TaylorSuite(308, True, datetime(2023, 3, 28))
  taylorsuite9 = TaylorSuite(309, True, datetime(2023, 3, 28))
  taylorsuite10 = TaylorSuite(310, True, datetime(2023, 3, 10))
  taylorsuite11 = TaylorSuite(311, True, datetime(2023, 3, 28))
  taylorsuite12 = TaylorSuite(312, True, datetime(2023, 3, 28))
  taylorsuite13 = TaylorSuite(313, True, datetime(2023, 3, 28))
  # TaylorSuite14 is used to ensure that the room cannot be created.
  # Because the hotel does not contain that many rooms.
  taylorsuite14 = TaylorSuite(313, True, datetime(2023, 3, 28))
  
  # Check if each suite instances were created properly.
  print(f"Type: {type(suite1)}, Room Number: {suite1.room_number}, Availability: {suite1.available}")
  print(f"Type: {type(suite2)}, Room Number: {suite2.room_number}, Availability: {suite2.available}")
  print(f"Type: {type(suite3)}, Room Number: {suite3.room_number}, Availability: {suite3.available}")
  print(f"Type: {type(suite4)}, Room Number: {suite4.room_number}, Availability: {suite4.available}")
  # Check if each stand room instances were created properly.
  print(f"Type: {type(standard1)}, Room Number: {standard1.room_number}, Availability: {standard1.available}")
  print(f"Type: {type(standard2)}, Room Number: {standard2.room_number}, Availability: {standard2.available}")
  print(f"Type: {type(standard3)}, Room Number: {standard3.room_number}, Availability: {standard3.available}")
  print(f"Type: {type(standard4)}, Room Number: {standard4.room_number}, Availability: {standard4.available}")
  # Check if each taylor suite instances were created properly.
  print(f"Type: {type(taylorsuite1)}, Room Number: {taylorsuite1.room_number}, Availability: {taylorsuite1.available}")
  print(f"Type: {type(taylorsuite2)}, Room Number: {taylorsuite2.room_number}, Availability: {taylorsuite2.available}")
  print(f"Type: {type(taylorsuite3)}, Room Number: {taylorsuite3.room_number}, Availability: {taylorsuite3.available}")
  print(f"Type: {type(taylorsuite4)}, Room Number: {taylorsuite4.room_number}, Availability: {taylorsuite4.available}")
  # Used to check instance when two many rooms are created. 
  print(f"Type: {type(taylorsuite14)}, Room Number: {taylorsuite14.room_number}, Availability: {taylorsuite14.available}")
  
  # Whitespace.
  print("\n")
  
  # Create a guest and check them into a room.
  guest1 = Guest('John Smith', datetime(2023,4,3), datetime(2023,4,5))
  guest2 = Guest('Anneth Sivakumar', datetime(2023,4,3), datetime(2023,4,6))
  guest3 = Guest('Mason Petri', datetime(2023,4,3), datetime(2023,4,7))
  # Instance where user forgets to enter date.
  #guest4 = Guest('Haris Khan', datetime(2023,4,5))
  guest4 = Guest('Owen Tucker', datetime(2023,3,9), datetime(2023,4,8))
  
  # Check if guest were intialized correctly.
  print(f"Name: {guest1.name}, Check-out-date: {guest1.check_out_date}")
  print(f"Name: {guest2.name}, Check-out-date: {guest2.check_out_date}")
  print(f"Name: {guest3.name}, Check-out-date: {guest3.check_out_date}")
  #print(f"Name: {guest4.name}, Check-out-date: {guest4.check_out_date}")
  
  # Whitespace.
  print("\n")
  
  # Test if guest_check_in books guest into available rooms.
  suite1.guest_check_in(guest1)
  print()
  standard1.guest_check_in(guest2)
  print()
  taylorsuite1.guest_check_in(guest3)
  print()
  suite1.guest_check_in(guest4)
  
  # Whitespace.
  print("\n")
  
  # Test services function.
  guest1.add_service("Food", 10)
  guest1.add_service("Massage", 120)
  guest2.add_service("Movie", 20)
  guest2.add_service("Arcade", 220)
  guest3.add_service("Movie", 40)
  guest3.add_service("Massage", 150)
  guest4.add_service("Movie", 40.24)
  guest3.add_service("Massage", 150.43)
  
  # Test send_bill.
  guest1.send_bill()
  print()
  guest2.send_bill()
  print()
  guest3.send_bill()
  print()
  guest4.send_bill()
  print()
  
  # Whitespace.
  print("\n")
  
  # Check if cleaning period is added to available date.
  # Should print 2023-04-06
  print(f"Room: {suite1.room_number}, New_Available_Date: {suite1.available_date}")
  # Should print 2023-04-06
  print(f"Room: {standard1.room_number}, New_Available_Date: {standard1.available_date}")
  # Should print 2023-04-09
  print(f"Room: {taylorsuite1.room_number}, New_Available_Date: {taylorsuite1.available_date}")


main()