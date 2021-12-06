class bingo:

    def __init__(self, numbers, board_rowlist):
        self.numbers = numbers
        self.boardcount = len(board_rowlist) // 5
        self.boards = self._gen_boards(board_rowlist)
        self.drawn = 0
        self.final_score = 0
        self.loser_score = 0

        print(self.boardcount)

    def _gen_boards(self, board_rowlist):
        """ Split a list of rows into an array of boards
            (a list of 2d arrays)
        """
        boards = []
        for i in range(self.boardcount):
            boards.append(self.board(board_rowlist[i*5:i*5+5]))
        return boards

    def _getscore(self, board, mynumbers):
        unmarked = board.unmarked_numbers(mynumbers)
        unmarked_score = sum([int(x) for x in unmarked])
        winning_number = int(mynumbers[-1])
        score = unmarked_score * winning_number
        print(f"score: {unmarked_score} x {winning_number} = {score}")
        return score

    def find_winner(self):
        for windex in range(5, len(self.numbers)):
            mynumbers = self.numbers[0:windex]
            # print(f"trying numbers: {mynumbers}")
            for board in self.boards:
                if board.iswinner(mynumbers):
                    print(f"winning numbers: {mynumbers}")
                    self.final_score = self._getscore(board, mynumbers)
                    return

    def find_last_winner(self):
        tboards = self.boards
        for windex in range(5, len(self.numbers)):
            mynumbers = self.numbers[0:windex]
            # print(f"trying numbers: {mynumbers}")
            winning_idx = []
            for idx, board in enumerate(tboards):
                if board.iswinner(mynumbers):
                    winning_idx.append(idx)
                    if len(tboards) == 1:
                        print(f"winning numbers: {mynumbers}")
                        self.loser_score = self._getscore(board, mynumbers)
                        return
            tboards = [b for i, b in enumerate(tboards) if i not in winning_idx]

    class board:

        def __init__(self, board):
            self.board = board

        def _test_board_rows(self, numbers):
            victory = False
            for row in self.board:
                matched = len(set(numbers) & set(row))
                if matched == 5:
                    # print(f"winner!: {row}")
                    victory = True
            return victory

        def _test_board_columns(self, numbers):
            victory = False
            for column in list(zip(*self.board))[0:]:
                matched = len(set(numbers) & set(column))
                if matched == 5:
                    # print(f"winner!: {column}")
                    victory = True
            return victory

        def covered_numbers(self, numbers):
            allnums = [x for y in self.board for x in y]
            covered = list(set(allnums) & set(numbers))
            return covered

        def unmarked_numbers(self, numbers):
            covered = self.covered_numbers(numbers)
            allnums = set([x for y in self.board for x in y])
            unmarked = allnums.difference(covered)
            return unmarked

        def iswinner(self, numbers):
            if self._test_board_rows(numbers) or \
                self._test_board_columns(numbers):
                return True

