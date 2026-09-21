class Solution:
    __boardLength = 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenInSection = {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (2, 0): set(),
            (2, 1): set(),
            (2, 2): set(),
        }

        for i in range(self.__boardLength):
            seenInRow = set()
            seenInColumn = set()
            for j in range(self.__boardLength):
                if board[i][j] != ".":
                    x, y = i // 3, j // 3
                    if board[i][j] in seenInRow or board[i][j] in seenInSection[(x, y)]:
                        return False
                    seenInRow.add(board[i][j])
                    seenInSection[(x, y)].add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in seenInColumn:
                        return False
                    seenInColumn.add(board[j][i])

        return True
