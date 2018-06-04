class Board:
    n, m, HEIGHT = 9, 9, 2
    LOWER_LEFT = [318, -86, HEIGHT]
    LOWER_RIGHT = [318, 86, HEIGHT]
    UPPER_LEFT = [132, -86, HEIGHT]
    UPPER_RIGHT = [132, 86, HEIGHT]
    unit_len = 1. * (LOWER_RIGHT[1] - LOWER_RIGHT[1]) / (n - 1)
    unit_wid = 1. * (LOWER_RIGHT[0] - UPPER_RIGHT[0]) / (m - 1)

    def location(self, x, y):
        ans = self.LOWER_LEFT
        ans[0] += x * self.unit_len
        ans[1] += y * self.unit_wid
        return ans


class ChessArea:
    def __init__(self):
        self.n, self.m, self.HEIGHT = 6, 7, -6
        self.pos = ((128, -104),)
        self.LOWER_LEFT = [318, -86, self.HEIGHT]
        self.idx = 0

    def location(self, idx):
        return [self.pos[idx][0], self.pos[idx][1], self.HEIGHT]

    @staticmethod
    def get_chess(self):
        self.idx += 1
        return self.location(self.idx - 1)


relay_point = [0, 0, 0]  # update
origin_point = [0, 0, 0]  # update
safe_pos = (130, -30, 15)
board = Board()
chess = ChessArea()
