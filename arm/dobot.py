import arm.DobotDll.DobotDllType as dType
from arm.location import chess, board, safe_pos
import os

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}
api = dType.load(os.getcwd() + '\\DobotDll\\')


def connect():
    state = dType.ConnectDobot(api, "", 115200)[0]  # Connect Dobot
    print("Connect status:", CON_STR[state])
    return state


def move_q(p):
    return dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, p[0], p[1], p[2], 0, 1)[0]


def move(p):
    # print(p)
    dType.SetQueuedCmdClear(api)
    last_idx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, p[0], p[1], p[2], 0, 1)[0]
    dType.SetQueuedCmdStartExec(api)
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)


def set_chess(x, y):
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    dType.SetHOMECmd(api, temp=0, isQueued=1)
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
    # 先让机械臂定位到指定的（x, y）坐标，并令z值处于较高位置，然后暂停0.5s后启动吸盘并降低机械臂
    # 然后提起棋子，移到指定位置上方暂停0.5s，然后下降并释放棋子，最后归零。
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    dType.SetHOMEParams(api, safe_pos[0], safe_pos[1], safe_pos[2], 0, isQueued=1)
    #dType.SetHOMECmd(api, temp=0, isQueued=1)
    move_q([117.39, -181.0795, 20])
    dType.SetWAITCmd(api, 0.5)
    move_q([117.39, -181.0795, -5])
    dType.SetWAITCmd(api, 0.5)
    dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)
    dType.SetWAITCmd(api, 0.5)
    move_q([127, -109, 20])
    dType.SetWAITCmd(api, 0.5)
    move_q([218.1596, 96.2065, -25])
    dType.SetWAITCmd(api, 0.5)
    dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1)
    dType.SetWAITCmd(api, 0.5)
    move_q([218.1596, 96.2065, 20])
    dType.SetWAITCmd(api, 0.5)
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
    if connect() == dType.DobotConnect.DobotConnect_NoError:
        take_chess_test()
        # set_chess(0, 0)
        # pass
    # dType.DisconnectDobot(api)  # Disconnect Dobot
