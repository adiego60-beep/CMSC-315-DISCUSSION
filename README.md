Unit 1 Discussion: Python OOP, Namespaces, and Copying
Project Overview
I built a small equipment management example to demonstrate object-oriented programming in Python. The program created equipment records, displayed equipment details, checked readiness, explored namespaces, and compared shallow and deep copying.
Design and Implementation
I created ParentClass with a shared equipment_category class variable and two instance attributes: name and serial_number. Its constructor checked that both values were provided, and display_info() returned basic equipment information.

I created ChildClass as a subclass of ParentClass. It added a class variable named equipment_type and instance attributes for location, status, and maintenance_history. I used super() to initialize the inherited fields and overrode display_info() to include the extra details. I also added add_maintenance() to record maintenance and check_readiness() as my student-created extension. The readiness method reported whether the status was operational or needed attention.

In demonstrate_namespaces(), I created two child objects, accessed a shared class variable through both the class and an instance, added an attribute to only one object, and printed the objects' __dict__ values and class namespace keys.

In demonstrate_copying(), I created an equipment object with a maintenance history list, made a shallow copy using copy() and a deep copy using deepcopy(), and then updated the original history. The shallow copy showed the new maintenance record because it shared the nested list. The deep copy kept its own list and did not show the new record.
How to Run
I used Python 3 and its built-in copy module. No additional packages were required.
python unit1_discussion.py
Testing
I ran the program to verify parent and child object creation, method overriding, inherited attributes, readiness changes, namespace output, and the difference between shallow and deep copies. I also tested empty equipment identifiers and empty maintenance records, which raised ValueError.
Reflection
I used an equipment example because it gave the assignment a practical purpose. Building the classes helped me see how shared code could be reused and how organizing attributes and methods together could make a program easier to update later.
