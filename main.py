# just, main
import time
from dobot import main as dobot
from myeye import main as myeye
from brain import main as brain


def work():
	last_state = myeye.see()
	while True:
		state = myeye.see()
		if state != last_state:
			last_state = state
			if brain.game_over(state): break
			x, y = brain.think(state)
			dobot.set_chess(x, y)
		time.sleep(1000)
	pass


if __name__ == '__main__':
	if dobot.connect() == dobot.dType.DobotConnect.DobotConnect_NoError:
		work()
	dobot.dType.DisconnectDobot(dobot.api)  # Disconnect Dobot
