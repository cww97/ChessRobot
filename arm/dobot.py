import arm.DobotDll.DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}
api = dType.load('DobotDll/')
safe_pos = (130, -30, 15)


def connect():
    state = dType.ConnectDobot(api, "", 115200)[0]  # Connect Dobot
    print("Connect status:", CON_STR[state])
    return state


def move_q(p):
    return dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, p[0], p[1], p[2], 0, 1)[0]


def move(p):
    print(p)
    dType.SetQueuedCmdClear(api)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, p[0], p[1], p[2], 0, 1)
    dType.SetQueuedCmdStartExec(api)
    dType.SetQueuedCmdStopExec(api)


class Board:
    n, m, HEIGHT = 9, 9, 2
    LOWER_LEFT = [318, -86, HEIGHT]
    LOWER_RIGHT = [318, 86, HEIGHT]
    UPPER_LEFT = [132, -86, HEIGHT]
    UPPER_RIGHT = [132, 86, HEIGHT]
    CENTER_POINT = [(LOWER_LEFT[0] + UPPER_LEFT[0]) / 2, (LOWER_LEFT[1] + LOWER_RIGHT[1]) / 2, HEIGHT]
    unit_len = 1. * (LOWER_RIGHT[1] - LOWER_RIGHT[1]) / (n - 1)
    unit_wid = 1. * (LOWER_RIGHT[0] - UPPER_RIGHT[0]) / (m - 1)


    
    def location(self, x, y):
        ans = self.LOWER_LEFT
        ans[0] += x * self.unit_len
        ans[1] += y * self.unit_wid
        return ans
    
    def down_chess(self, x, y):
        move(self.location(x, y))
        dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1)


# need to be updated
class ChessArea:
    n, m, HEIGHT = 6, 7, -5  # n: row, m: col

    pos = ((-12, 163), )
    LOWER_LEFT = [318, -86, HEIGHT]
    idx = 0
    
    def location(self, idx):
        ans = self.LOWER_LEFT
        ans[0] = self.pos[idx][0]
        ans[1] = self.pos[idx][1]
        return ans
        
    @staticmethod
    def get_chess(self):
        move(self.location(self.idx))
        self.idx += 1
        dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)


relay_point = [0, 0, 0]  # update
origin_point = [0, 0, 0]  # update
board = Board()
chess = ChessArea()


def set_chess(x, y):
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    chess.get_chess()
    move(relay_point)
    board.down_chess(x, y)
    last_idx = move(origin_point)

    dType.SetQueuedCmdStartExec(api)  # Start to Execute Command Queued
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:  # Wait for Executing Last Command
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)  # Stop to Execute Command Queued


def move_around():  # just for test
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    move_q(board.LOWER_LEFT)
    move_q(board.LOWER_RIGHT)
    move_q(board.UPPER_RIGHT)
    move_q(board.UPPER_LEFT)
    last_idx = move_q(board.CENTER_POINT)
    dType.SetQueuedCmdStartExec(api)  # Start to Execute Command Queued
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:  # Wait for Executing Last Command
        # print(dType.GetQueuedCmdCurrentIndex(api)[0])
        dType.dSleep(3000)
    dType.SetQueuedCmdStopExec(api)  # Stop to Execute Command Queued


def take_chess_test():
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    move_q([128.53, -104.25, 20])
    dType.SetWAITCmd(api, 0.5)
    move_q([128.53, -104.25, -6])
    dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)
    dType.SetWAITCmd(api, 1)
    move_q([127, -109, 20])
    dType.SetWAITCmd(api, 1)
    move_q([230.5, 47, 3])
    dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1)
    dType.SetWAITCmd(api, 0.5)
    move_q([233, 42, 20])
    dType.SetWAITCmd(api, 1.5)
    last_idx = move_q(safe_pos)
    dType.SetQueuedCmdStartExec(api)  # Start to Execute Command Queued
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:  # Wait for Executing Last Command
        print(dType.GetQueuedCmdCurrentIndex(api)[0])
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)  # Stop to Execute Command Queued

def take_move(move):
    # input like [x,y] list
    print('current arm move at :')
    print(move)


if __name__ == '__main__':
    test_board = Board()
    if connect() == dType.DobotConnect.DobotConnect_NoError:
        take_chess_test()
    dType.DisconnectDobot(api)  # Disconnect Dobot
