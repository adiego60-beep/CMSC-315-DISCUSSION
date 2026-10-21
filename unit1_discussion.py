
"""Unit 1: Python OOP, namespaces, and copying using equipment records."""
from copy import copy, deepcopy


class ParentClass:
    equipment_category = "General equipment"

    def __init__(self, name, serial_number):
        if not name or not serial_number:
            raise ValueError("Equipment name and serial number are required")
        self.name = name
        self.serial_number = serial_number

    def display_info(self):
        return f"{self.name} (Serial: {self.serial_number})"


class ChildClass(ParentClass):
    equipment_type = "Tracked equipment"

    def __init__(self, name, serial_number, location, status, maintenance_history=None):
        super().__init__(name, serial_number)
        self.location = location
        self.status = status
        self.maintenance_history = list(maintenance_history) if maintenance_history is not None else []

    def display_info(self):
        return f"{super().display_info()} | Location: {self.location} | Status: {self.status}"

    def add_maintenance(self, record):
        if not record:
            raise ValueError("Maintenance record cannot be empty")
        self.maintenance_history.append(record)

    def check_readiness(self):
        return "Ready for use" if self.status.strip().lower() == "operational" else "Needs attention"


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first = ChildClass("Radio", "R-100", "Storage", "Operational")
    second = ChildClass("Laptop", "L-200", "Office", "Maintenance")
    print("Class variable through class:", ParentClass.equipment_category)
    print("Same class variable through object:", first.equipment_category)
    print("Child class variable:", ChildClass.equipment_type)
    first.assigned_to = "Team A"
    print("First object's namespace:", first.__dict__)
    print("Second object's namespace:", second.__dict__)
    print("Parent class namespace keys:", list(ParentClass.__dict__.keys()))
    print("Child class namespace keys:", list(ChildClass.__dict__.keys()))
    print("Only first object has assigned_to:", hasattr(first, "assigned_to") and not hasattr(second, "assigned_to"))


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ChildClass("Generator", "G-300", "Motor Pool", "Operational", ["Initial inspection"])
    shallow = copy(original)
    deep = deepcopy(original)
    original.add_maintenance("Oil change")
    print("Original history:", original.maintenance_history)
    print("Shallow copy history:", shallow.maintenance_history)
    print("Deep copy history:", deep.maintenance_history)
    # A shallow copy makes a new outer object but shares its nested list.
    # A deep copy makes a new outer object and an independent nested list.
    print("Shallow shares history list:", original.maintenance_history is shallow.maintenance_history)
    print("Deep shares history list:", original.maintenance_history is deep.maintenance_history)


def main():
    print("=== Unit 1 OOP Assignment ===")
    parent = ParentClass("Printer", "P-001")
    child = ChildClass("Radio", "R-100", "Storage", "Operational")
    print("\nParent:", parent.display_info())
    print("Child (overridden method):", child.display_info())
    print("Inherited name:", child.name)
    print("Readiness:", child.check_readiness())
    child.status = "Maintenance"
    print("Readiness after status change:", child.check_readiness())
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
