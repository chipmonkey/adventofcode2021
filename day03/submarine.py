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

    @staticmethod
    def _binstr_to_int(binstr):
        if isinstance(binstr, list):
            binstr= ''.join([str(i) for i in binstr])
        bint = int(binstr, 2)
        return bint

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

    def oxygen_rating(self):
        oreport = self.report
        remaining = len(oreport)
        position = 0
        while remaining > 1:
            thing = oreport[position].mode()
            if len(thing) > 1:
                ostr = '1'
            else:
                ostr = ''.join([str(i) for i in list(oreport[position].mode().loc[0])])
            oreport = [list(x[1]) for x in oreport.iterrows() if x[1][position] == ostr]
            oreport = pd.DataFrame(oreport)
            remaining = len(oreport)
            position += 1
        return self._binstr_to_int(list(oreport.loc[0]))

    def carbon_rating(self):
        creport = self.report
        remaining = len(creport)
        position = 0
        while remaining > 1:
            thing = creport[position].mode()
            if len(thing) > 1:
                cstr = '1'
            else:
                cstr = ''.join([str(i) for i in list(creport[position].mode().loc[0])])
            cstr = '0' if cstr == '1' else '1'
            creport = [list(x[1]) for x in creport.iterrows() if x[1][position] == cstr]
            creport = pd.DataFrame(creport)
            remaining = len(creport)
            position += 1
        return self._binstr_to_int(list(creport.loc[0]))
