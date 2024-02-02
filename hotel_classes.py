"""
CISC-121 2023W
Name: <Anneth Sivakumar>
Student Number: <20320973>
Email: <21as221@queensu.ca>
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
from datetime import *

class HotelRoom:
  """
  -------------------------------------------------------
  A class representing a hotel room.
  -------------------------------------------------------
  Attributes:
      room_number (int): the room number.
      available (bool): indicates if the room is available for booking.
  -------------------------------------------------------
  """
  
  def __init__(self, room_number, available):
    """
    -------------------------------------------------------
    Initializes a HotelRoom object.
    -------------------------------------------------------
    Parameters:
        room_number (int): the room number.
        available (bool): indicates if the room is available for booking.
    Returns:
        None.
    -------------------------------------------------------
    """
    # Increment the count of rooms based on the type of room.
    # Hotel cannot exceed 19 suites, 13 taylor suites and 89 standard rooms.
    if isinstance(self, Suite):
      if Suite.num_suites >= 19:
        print("No more suites available")
      Suite.num_suites += 1
    elif isinstance(self, TaylorSuite):
      if TaylorSuite.num_taylor_suites >= 13:
        print("No more taylor suites available")
      TaylorSuite.num_taylor_suites += 1
    else:
      if StandardRoom.num_standard_rooms >= 89:
        print("No more standard rooms available")
      StandardRoom.num_standard_rooms += 1
    self.room_number = room_number
    self.available = available

  def guest_check_in(self, some_guest):
    """
    -------------------------------------------------------
    Checks a guest into a room and updates availability.
    -------------------------------------------------------
    Parameters:
        some_guest – the guest checking in (guest object).
    Returns:
        None.
    -------------------------------------------------------
    """
    # Check if guest check in date is before the available date.
    if self.available_date > some_guest.check_in_date:
      # Print the date the room will be available if not currently available.
      print(f"Room {self.room_number}, Not Available Until: {self.available_date}")
    # Otherwise, book in the guest for that room if the room is available.
    elif self.available:
      # Print the availability of the room.
      print(f"Room {self.room_number}, Available: {self.available_date}")
      self.available = False
      # Determine the number of days the room will be unavailable based on room type.
      if isinstance(self, Suite):
        self.available_date = some_guest.check_out_date + timedelta(days=1)
      elif isinstance(self, TaylorSuite):
        self.available_date = some_guest.check_out_date + timedelta(days=2)
      else:
        self.available_date = some_guest.check_out_date + timedelta(days=0)
      # Print the updated availability status of the room.
      print(f"Name: {some_guest.name}, Room {self.room_number}, Available: {self.available}   ~Booked!")
    else:
      # Print a message indicating the room is not available.
      print(f"Room {self.room_number}, Not Available")


class Suite(HotelRoom):
  """
  -------------------------------------------------------
  A class representing a suite.
  -------------------------------------------------------
  Attributes:
     room_number (int): the room number.
     available (bool): indicates if the room is available for booking.
     available_date (date): the date when the room becomes available again.
  -------------------------------------------------------
  """
  # Create variable to keep track of number of suites.
  num_suites = 0
  
  def __init__(self, room_number, available, available_date):
    """
    -------------------------------------------------------
    Initializes a Suite object.
    -------------------------------------------------------
    Parameters:
        room_number (int): the room number.
        available (bool): indicates if the room is available for booking.
        available_date (date): the date when the room becomes available again.
    Returns:
        None.
    -------------------------------------------------------
    """
    super().__init__(room_number, available)
    self.available_date = available_date


class StandardRoom(HotelRoom):
  """
  -------------------------------------------------------
  A class representing a standard room.
  -------------------------------------------------------
  Attributes:
      room_number (int): the room number.
      available (bool): indicates if the room is available for booking.
      available_date (date): the date when the room becomes available again.
  -------------------------------------------------------
  """
  # Create variable to keep track of number of suites.
  num_standard_rooms = 0
  
  def __init__(self, room_number, available, available_date):
    """
    -------------------------------------------------------
    Initializes a StandardRoom object.
    -------------------------------------------------------
    Parameters:
        room_number (int): the room number.
        available (bool): indicates if the room is available for booking.
        available_date (date): the date when the room becomes available again.
    Returns:
        None.
    -------------------------------------------------------
    """
    super().__init__(room_number, available)
    self.available_date = available_date


class TaylorSuite(HotelRoom):
  """
  -------------------------------------------------------
  A class representing a taylor suite.
  -------------------------------------------------------
  Attributes:
      room_number (int): the room number.
      available (bool): indicates if the room is available for booking.
      available_date (date): the date when the room becomes available again.
  -------------------------------------------------------
  """
  # Create variable to keep track of number of suites.
  num_taylor_suites = 0
  
  def __init__(self, room_number, available, available_date):
    """
    -------------------------------------------------------
    Initializes a TaylorSuite object.
    -------------------------------------------------------
    Parameters:
        room_number (int): the room number.
        available (bool): indicates if the room is available for booking.
        available_date (date): the date when the room becomes available again.
    Returns:
        None.
    -------------------------------------------------------
    """
    super().__init__(room_number, available)
    self.available_date = available_date


class Service:
  """
  -------------------------------------------------------
  A class representing the services the guest has used during their stay.
  -------------------------------------------------------
  Attributes:
      name (str): the name of the service.
      cost (int): the cost of the service.
  -------------------------------------------------------
  """
  def __init__(self, name, cost):
    """
    -------------------------------------------------------
    Initializes a new Service object.
    -------------------------------------------------------
    Parameters:
        name (str): The name of the service.
        cost (int): The cost of the service.
    Returns:
        None.
    -------------------------------------------------------
    """
    self.name = name
    self.cost = cost


class Guest:
  def __init__(self, name, check_in_date, check_out_date):
    """
    -------------------------------------------------------
    Initializes a new Guest object.
    -------------------------------------------------------
    Parameters:
        name (str): The name of the guest.
        check_in_date (datetime): The date the guest checks in.
        check_out_date (datetime): The date the guest checks out.
    Returns:
        None.
    -------------------------------------------------------
    """
    self.name = name
    self.check_out_date = check_out_date
    self.check_in_date = check_in_date
    self.services = []
    self.total_bill = 0

  def add_service(self, service_name, service_cost):
    """
    -------------------------------------------------------
    Adds a service to the bill of a guest.
    -------------------------------------------------------
    Parameters:
        service_name (str): name of service.
        service_cost (int): cost of the service.
    Returns: None.
    -------------------------------------------------------
    """
    if isinstance(service_cost, int):
      new_service = Service(service_name, service_cost)
      # Store service in services list.
      self.services.append(new_service)
      # Sum up all the prices.
      self.total_bill += new_service.cost
    else:
      print("ERROR: Please Enter Integer Prices!")

  def send_bill(self):
    """
    -------------------------------------------------------
    Based on the total services and bill total provides a
    Printed statement of all services with the total cost.
    -------------------------------------------------------
    Parameters:
        None.
    Returns:
        None.
    -------------------------------------------------------
    """
    # Print guest's bill contents and final total.
    print(f"Bill for {self.name}:")
    for service in self.services:
      print(f"{service.name}: ${service.cost}")
    print("\n" + f"Total: ${self.total_bill}")
