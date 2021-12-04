import pandas as pd

class submarine:

    def __init__(self):
        self.hpos = 0  # Horizontal Position
        self.depth = 0 # Depth
        self.aim = 0   # Aim
        self.report = pd.DataFrame([])

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

    @staticmethod
    def _gamma_rate(report):
        gamma = report.mode()
        gstr = ''.join([str(i) for i in list(gamma.loc[0])])
        gint = int(gstr, 2)
        return gint

    @staticmethod
    def _epsilon_rate(report):
        epsilon = report.mode()
        estr = ['0' if x == '1' else '1' for x in list(epsilon.loc[0])]
        estr = ''.join([i for i in estr])
        eint = int(estr, 2)
        return eint

    def set_report(self, input):
        self.report = pd.DataFrame(input)
        print(f"report is: {self.report}")

    
