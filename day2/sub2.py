class sub2:

    def __init__(self):
        self.hpos = 0  # Horizontal Position
        self.depth = 0 # Depth
        self.aim = 0   # Aim

    def _forward(self, dist):
        self.hpos = self.hpos + dist
        self.depth = self.depth + (self.aim * dist)

    def _down(self, dist):
        self.aim = self.aim + dist

    def _up(self, dist):
        self.aim = self.aim - dist

    def move(self, movestr):
        (direction, distance) = movestr.split(' ')
        distance = int(distance)
        if direction == 'forward':
            self._forward(distance)
        elif direction == 'down':
            self._down(distance)
        elif direction == 'up':
            self._up(distance)
#        print(f"{movestr}: hpos: {self.hpos} depth: {self.depth} aim: {self.aim}")
