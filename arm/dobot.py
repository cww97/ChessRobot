import arm.DobotDll.DobotDllType as dType
import os

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}
api = dType.load(os.getcwd() + '\\DobotDll\\')

safe_pos = (130, -30, 15)


def connect():
    state = dType.ConnectDobot(api, "", 115200)[0]  # Connect Dobot
    print("Connect status:", CON_STR[state])
    return state


def move_q(p):
    dType.SetWAITCmd(api, 0.5)
    return dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, p[0], p[1], p[2], 0, 1)[0]


def move(p):
    # print(p)
    dType.SetQueuedCmdClear(api)
    last_idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, p[0], p[1], p[2], 0, 1)[0]
    dType.SetQueuedCmdStartExec(api)
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)


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
        self. pos = ((128, -104),)
        self.LOWER_LEFT = [318, -86, self.HEIGHT]
        self.idx = 0
    
    def location(self, idx):
        return [self.pos[idx][0], self.pos[idx][1], self.HEIGHT]
        
    @staticmethod
    def get_chess(self):
        self.idx += 1
        return self.location(self.idx-1)


relay_point = [0, 0, 0]  # update
origin_point = [0, 0, 0]  # update
board = Board()
chess = ChessArea()


def set_chess(x, y):
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    chess_pos = chess.get_chess(chess)
    chess_pos_h = chess_pos
    chess_pos_h[2] += 30
    move_q(chess_pos_h)
    move_q(chess_pos)
    print('chess_pos = ', chess_pos)
    dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)
    move_q(chess_pos_h)
    board_pos = board.location(x, y)
    board_pos_h = board_pos
    board_pos_h[2] += 30
    move_q(board_pos_h)
    move_q(board_pos)
    dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1)
    last_idx = move_q(safe_pos)
    dType.SetQueuedCmdStartExec(api)  # Start to Execute Command Queued
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:  # Wait for Executing Last Command
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)  # Stop to Execute Command Queued


# 落子的demo
def take_chess_test():
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    move_q([128.53, -104.25, 20])
    move_q([128.53, -104.25, -6])
    dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)
    move_q([127, -109, 20])
    move_q([230.5, 47, 3])
    dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1 )
    move_q([233, 42, 20])
    last_idx = move_q(safe_pos)
    dType.SetQueuedCmdStartExec(api)  # Start to Execute Command Queued
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:  # Wait for Executing Last Command
        # print(dType.GetQueuedCmdCurrentIndex(api)[0])
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)  # Stop to Execute Command Queued


def take_move(move):
    # input like [x,y] list
    print('current arm move at :')
    print(move)


if __name__ == '__main__':
    if connect() == dType.DobotConnect.DobotConnect_NoError:
        # take_chess_test()
        set_chess(0, 0)
        pass
    dType.DisconnectDobot(api)  # Disconnect Dobot
