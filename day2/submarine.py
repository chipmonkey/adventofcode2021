class submarine:

    def __init__(self):
        self.hpos = 0  # Horizontal Position
        self.depth = 0 # Depth

    def _forward(self, dist):
        self.hpos = self.hpos + dist

    def _down(self, dist):
        # print(f"moving depth from {self.depth} by {dist}")
        self.depth = self.depth + dist
        # print(f"depth is now: {self.depth}")

    def _up(self, dist):
        self.depth = self.depth - dist

    def move(self, movestr):
        (direction, distance) = movestr.split(' ')
        distance = int(distance)
        if direction == 'forward':
            self._forward(distance)
        elif direction == 'down':
            self._down(distance)
        elif direction == 'up':
            self._up(distance)
