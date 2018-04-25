# just main for dobot
import DobotDll.DobotDllType as dType
import DobotBoard
import DobotChess
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}
api = dType.load()
# --------------------------- const ------------------------------


def move(point):
    return dType.SetPTPCmd(api, MOVE_MODE, point[0], point[1], point[2], 0, 1)[0]


def dobot_work():
    dobot_init()

    # Async PTP Motion
    # lastIndex = dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)

    lastIndex = move(LOWER_LEFT)
    lastIndex = move(LOWER_RIGHT)
    lastIndex = move(UPPER_RIGHT)
    lastIndex = move(UPPER_LEFT)
    lastIndex = move(CENTER_POINT)
    lastIndex = move()

    # lastIndex = dType.SetPTPCmd(api, MOVE_MODE, 134, 0, 15, 0, isQueued=1)[0]
    # lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 230, 0, 15, 0, isQueued=1)[0]
    # lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 230, 0, -30, 0, isQueued=1)[0]
    # lastIndex = dType.SetEndEffectorSuctionCup(api, True, False, isQueued=1)

    # Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    # Wait for Executing Last Command
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(2000)

    # Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)


def dobot_init():
    # Clean Command Queued
    dType.SetQueuedCmdClear(api)
    # Async Motion Params Setting
    dType.SetHOMEParams(api, CENTER_POINT[0], CENTER_POINT[1], CENTER_POINT[2], 0, isQueued=1)  # 设置回零参数
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued=1)  # 设置关节点位参数
    dType.SetPTPCommonParams(api, 50, 50, isQueued=1)  # 设置点位公共参数

    # Async Home 执行回零功能
    dType.SetHOMECmd(api, temp=0, isQueued=1)


def main():
    # Connect Dobot
    state = dType.ConnectDobot(api, "", 115200)[0]
    print("Connect status:", CON_STR[state])

    if state == dType.DobotConnect.DobotConnect_NoError:
        dobot_work()

    # Disconnect Dobot
    dType.DisconnectDobot(api)


if __name__ == '__main__':
    main()
