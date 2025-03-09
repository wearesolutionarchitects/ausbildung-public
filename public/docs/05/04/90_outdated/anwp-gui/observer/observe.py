from abc import ABC, abstractmethod

# Observable (Subject)
class Customer(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class User(Customer):
    def __init__(self, name, status="inactive"):
        super().__init__()
        self._name = name
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status
        self.notify_observers()

    def __str__(self):
        return f"User: {self._name}, Status: {self._status}"

# Observer (Staff)
class Staff(ABC):
    @abstractmethod
    def update(self, user):
        pass

class SupportStaff(Staff):
    def update(self, user):
        print(f"Support Staff notified about status change: {user}")

class SalesStaff(Staff):
    def update(self, user):
        print(f"Sales Staff notified about status change: {user}")

# Test the observer pattern
if __name__ == "__main__":
    # Create a user
    user1 = User("Curt Cobain")

    # Create staff members
    support_staff = SupportStaff()
    sales_staff = SalesStaff()

    # Add staff members as observers
    user1.add_observer(support_staff)
    user1.add_observer(sales_staff)

    # Change user status
    print("Updating user status to 'active'...")
    user1.status = "active"

    print("Updating user status to 'inactive'...")
    user1.status = "inactive"
