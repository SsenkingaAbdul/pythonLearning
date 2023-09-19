class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = []
    
    def getcapacity(self):
        return self.capacity - len(self.seats)

    def add_passenger(self, name):
        if not self.getcapacity():
            return False
        self.seats.append(name)
        return True

    
p = Flight(3)
passenger = ["James", "Abdul", "Amos", "Noah"]
for person in passenger:
    if p.add_passenger(person):
        print(f"Added {person} to the flight")
    else:
        print(f"{person} has not been added to the flight")            