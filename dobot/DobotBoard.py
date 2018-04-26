import DobotDll.DobotDllType as dType

MOVE_MODE = dType.PTPMode.PTPMOVLXYZMode
BOARD_HEIGHT = 2
LOWER_LEFT = [318, -86, BOARD_HEIGHT]
LOWER_RIGHT = [318, 86, BOARD_HEIGHT]
UPPER_LEFT = [132, -86, BOARD_HEIGHT]
UPPER_RIGHT = [132, 86, BOARD_HEIGHT]
CENTER_POINT = [(LOWER_LEFT[0] + UPPER_LEFT[0]) / 2, (LOWER_LEFT[1] + LOWER_RIGHT[1]) / 2, BOARD_HEIGHT]
# -------------------------------- -const ---------------------------------------------


