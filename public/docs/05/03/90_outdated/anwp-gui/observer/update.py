from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, reservation):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, reservation):
        for observer in self._observers:
            observer.update(reservation)

class ReservationSystem(Subject):
    def __init__(self):
        super().__init__()
        self._reservations = []

    def add_reservation(self, reservation):
        self._reservations.append(reservation)
        self.notify(reservation)

    def update_reservation(self, reservation_id, new_details):
        for reservation in self._reservations:
            if reservation.id == reservation_id:
                reservation.details = new_details
                self.notify(reservation)
                break

class Reservation:
    def __init__(self, reservation_id, details):
        self.id = reservation_id
        self.details = details

class EmailNotifier(Observer):
    def update(self, reservation):
        # Hier würde der Code zum Senden einer E-Mail stehen
        print(f"E-Mail gesendet für aktualisierte Reservierung: {reservation.id}")

# Beispielverwendung
if __name__ == "__main__":
    reservation_system = ReservationSystem()
    email_notifier = EmailNotifier()
    reservation_system.attach(email_notifier)

    reservation1 = Reservation(1, "Details zur Reservierung 1")
    reservation_system.add_reservation(reservation1)

    # Aktualisiere die Reservierung
    reservation_system.update_reservation(1, "Aktualisierte Details zur Reservierung 1")
