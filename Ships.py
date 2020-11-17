class Ship:
    def __init__(self, arrival_time, arrival_position):
        self.arrival_time = arrival_time
        self.arrival_position = arrival_position


T = 20
ship1 = Ship(0, 0)
ship2 = Ship(5, 1)
ship3 = Ship(30, 0)
ship4 = Ship(50, 1)
ship5 = Ship(85, 1)
ship6 = Ship(110, 0)

arrival_times = []
arrival_positions = []

ships = [ship1, ship2, ship3, ship4, ship5, ship6]

for ship in ships:
    arrival_times.append(ship.arrival_time)
    arrival_positions.append(ship.arrival_position)
