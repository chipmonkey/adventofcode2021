class fish:

    def __init__(self, fish):
        self.fish = fish
        self.counts = self._initcount()

    def _spawn(self):
        self.fish = [x-1 for x in self.fish]
        new = self.fish.count(-1)
        self.fish = [x if x >= 0 else 6 for x in self.fish]
        newl = [8]*new
        self.fish.extend(newl)
        # print(self.fish)

    def thing(self):
        for i in range(100):
            print(f"day: {i} fish: {len(self.fish)}")
            self._spawn()
        return len(self.fish)


    def _initcount(self):
        self.counts = {}
        for i in range(9):
            self.counts[i] = 0

        for x in self.fish:
            self.counts[x] += 1

        print(self.counts)
        return self.counts

    def _quickspawn(self):
        newcounts = {}
        for i in range(9):
            newcounts[i] = 0

        for key in self.counts:
            if key == 0:
                newcounts[8] = self.counts[key]
                newsix = self.counts[key]
            else:
                newcounts[key - 1] = self.counts[key]
        newcounts[6] += newsix

        self.counts = newcounts
        # print(self.counts)

    def thing2(self):
        for i in range(300):
            print(f"day: {i} fish: {sum(self.counts.values())}")
            self._quickspawn()
