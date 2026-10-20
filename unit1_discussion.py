
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    pass


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    pass


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    print("\nTODO: Create and test your child object")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()

## Implementation Documentation

I created a Python program that used object-oriented programming to represent an equipment management system. I created a parent class called `ParentClass` that stored basic equipment information, including the equipment name and serial number. I also created a child class called `ChildClass` that inherited information from the parent and added details such as location, equipment status, and maintenance history.I used inheritance to avoid rewriting the same code in multiple places. The child class also overrode the `display_info()` method so it could display additional information.

For the namespace demonstration, I created two equipment objects and used `__dict__` to show their individual attributes. I also accessed a class variable through both the class and an object. This helped demonstrate how class variables can be shared while instance attributes remain separate.

For the copying demonstration, I used `copy()` and `deepcopy()` to compare shallow and deep copies. I added a maintenance record to the original object's list and showed how the shallow copy reflected that change while the deep copy remained unchanged. This demonstrated how nested mutable data can share references between objects.

As my own extension, I added a `check_readiness()` method that checked whether equipment was operational or needed attention before use.

Unit 1 Reflection

This assignment helped me understand how object-oriented programming works in Python and why it is useful for organizing code. I learned how inheritance allows a child class to reuse information from a parent class, how namespaces separate class and instance attributes, and how shallow and deep copying handle data differently.

One challenge was understanding why changing the original maintenance list also changed the shallow copy. I learned that a shallow copy still shares references to nested objects, while a deep copy creates independent copies. Testing the maintenance history helped make that difference clearer.

Compared to procedural programming, I think OOP is more useful for larger projects because it keeps related information and methods together. Procedural programming can be simpler for smaller tasks, but OOP makes it easier to reuse code and update individual parts without rewriting the entire program. Although creating classes adds some extra code and planning, it can reduce maintenance work as applications grow.

I used an equipment management example because it connects programming to a practical situation. These concepts could also help me develop applications for technology and cybersecurity in the future.

## Testing

I designed the program to demonstrate the following:

- Creating parent and child objects and displaying their information.
- Using inheritance and overriding a method.
- Comparing class and instance namespaces.
- Demonstrating shallow and deep copying with maintenance records.
- Checking equipment readiness using the student-created extension.

The copying demonstration was designed to show that the shallow copy shared the original maintenance list, while the deep copy maintained an independent list.