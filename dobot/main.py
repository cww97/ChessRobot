# just main for dobot
import DobotDll.DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}
api = dType.load()

MOVE_MODE = dType.PTPMode.PTPMOVLXYZMode
# ---------------------------------- board -------------------------------------------
BOARD_HEIGHT = 2
BOARD_LOWER_LEFT = [318, -86, BOARD_HEIGHT]
BOARD_LOWER_RIGHT = [318, 86, BOARD_HEIGHT]
BOARD_UPPER_LEFT = [132, -86, BOARD_HEIGHT]
BOARD_UPPER_RIGHT = [132, 86, BOARD_HEIGHT]
BOARD_CENTER_POINT = [(BOARD_LOWER_LEFT[0] + BOARD_UPPER_LEFT[0]) / 2,
                      (BOARD_LOWER_LEFT[1] + BOARD_LOWER_RIGHT[1]) / 2, BOARD_HEIGHT]
# ---------------------------------- chess -------------------------------------------
# need to be updated
CHESS_HEIGHT = 2
CHESS_LOWER_LEFT = [318, -86, BOARD_HEIGHT]
CHESS_LOWER_RIGHT = [318, 86, BOARD_HEIGHT]
CHESS_UPPER_LEFT = [132, -86, BOARD_HEIGHT]
CHESS_UPPER_RIGHT = [132, 86, BOARD_HEIGHT]
CHESS_CENTER_POINT = [(BOARD_LOWER_LEFT[0] + BOARD_UPPER_LEFT[0]) / 2,
                      (BOARD_LOWER_LEFT[1] + BOARD_LOWER_RIGHT[1]) / 2, BOARD_HEIGHT]

# ---------------------------------- const -------------------------------------------


def connect():
    state = dType.ConnectDobot(api, "", 115200)[0]  # Connect Dobot
    print("Connect status:", CON_STR[state])
    return state


def move(p):
    return dType.SetPTPCmd(api, MOVE_MODE, p[0], p[1], p[2], 0, 1)[0]


def dobot_work():
    # lastIndex = dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)
    # lastIndex = dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1)
    dType.SetQueuedCmdClear(api)  # Clean Command Queued
    move(BOARD_LOWER_LEFT)
    move(BOARD_LOWER_RIGHT)
    move(BOARD_UPPER_RIGHT)
    move(BOARD_UPPER_LEFT)
    last_idx = move(BOARD_CENTER_POINT)

    dType.SetQueuedCmdStartExec(api)  # Start to Execute Command Queued
    while last_idx > dType.GetQueuedCmdCurrentIndex(api)[0]:  # Wait for Executing Last Command
        dType.dSleep(100)
    dType.SetQueuedCmdStopExec(api)  # Stop to Execute Command Queued


def get_chess():
    pass


def set_chess(x, y):
    pass


def main():
    if connect() == dType.DobotConnect.DobotConnect_NoError:
        dobot_work()
    dType.DisconnectDobot(api)  # Disconnect Dobot


if __name__ == '__main__':
    main()
