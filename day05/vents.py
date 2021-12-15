import numpy as np

class vents2:

    def __init__(self, segments):
        self.segments = segments
        (self.maxx, self.maxy) = self._getmaxxy()
        self.board = np.zeros((self.maxx+1, self.maxy+1),  dtype=int)

    def _getmaxxy(self):
        allxs = [x[0] for x in self.segments]
        allxs.extend([x[2] for x in self.segments])
        allys = [x[1] for x in self.segments]
        allys.extend([x[3] for x in self.segments])
        print(f"segments: {self.segments}")
        print([x[0] for x in self.segments])
        print([x[2] for x in self.segments])
        print(f"allxs: {allxs}")
        maxx = max(allxs)
        maxy = max(allys)
        print(f"(maxx, maxy): ({maxx}, {maxy})")
        return (int(maxx), int(maxy))

    def _draw_vertical(self, s):
        print(f"draw vertical: {s}")
        x = s[0]
        if s[3] < s[1]:
            (start, fin) = (s[3], s[1])
        else:
            (start, fin) = (s[1], s[3])
        for y in range(start, fin+1):
            self.board[x, y] += 1
        print(np.transpose(self.board))
        

    def _draw_horizontal(self, s):
        print(f"draw horizontal: {s}")
        y = s[1]
        if s[2] < s[0]:
            (start, fin) = (s[2], s[0])
        else:
            (start, fin) = (s[0], s[2])
        for x in range(start, fin+1):
            self.board[x, y] += 1
        print(np.transpose(self.board))

    def _draw_diagonal(self, s):
        print(f"draw diagonal: {s}")
        if s[2] < s[0]:
            xvals = list(range(s[0], s[2]-1, -1))
        else:
            xvals = list(range(s[0], s[2]+1, 1))

        if s[3] < s[1]:
            yvals = list(range(s[1], s[3]-1, -1))
        else:
            yvals = list(range(s[1], s[3]+1, 1))

        # xdir = int((s[2]-s[0])/abs(s[2]-s[0]))
        # ydir = int((s[3]-s[1])/abs(s[3]-s[1]))

        print(f"xvals: {xvals}")
        print(f"yvals: {yvals}")

        for (x, y) in zip(xvals, yvals):
            self.board[x, y] += 1
        print(np.transpose(self.board))

    def _build_board(self):
        for s in self.segments:
            if s[0] == s[2]:
                self._draw_vertical(s)
            if s[1] == s[3]:
                self._draw_horizontal(s)
            if abs(s[2] - s[0]) == abs(s[3] - s[1]):
                self._draw_diagonal(s)

    def count_overlaps(self):
        print(self.board)
        self._build_board()
        return np.count_nonzero(self.board > 1)
