# just, main
import dobot.main as dobot


def work():
    pass


def main():
    if dobot.connect() == dobot.dType.DobotConnect.DobotConnect_NoError:
        work()
    dobot.dType.DisconnectDobot(dobot.api)  # Disconnect Dobot


def main():
	pass


if __name__ == '__main__':
	main()
