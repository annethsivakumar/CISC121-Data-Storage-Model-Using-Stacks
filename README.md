Scenario: 
---------
You are working on creating a data storage model for a local hotel. Each day they have people
arriving who will be booked into different types of rooms: suites, standard, and executive suites
they have branded as Taylor Suites.

The hotel rooms each have a room number stored as an integer and are marked as either
available or unavailable (true or false). Each room is marked as unavailable until the check out
date for the guests. Each different suite type has an available date. These rooms are difficult to
clean, so once a guest checks out, the room will not be available until 1 day later for the suites,
and 2 days later for the Taylor Suites, standard rooms are available on the same day. [Hint: The
availability date is different for each room type].

Every person arrives with a check out date. They are assigned to a type of room. The hotel
keeps track of which guests are in each room, and when the check out date for each room is.
There are 19 suites, 89 standard rooms, and 13 Taylor Suites. Each guest has a name, a check
out date, a list of services they receive (such as room service, or movies), and a total bill (an
integer value) to be given at the end of their stay.

The services are also stored in this system as a class and contain a service name and a cost for
that particular service.
