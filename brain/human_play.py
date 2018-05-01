from __future__ import print_function
from brain.game import Board, Game
from myeye.eye_control import take_input
from brain.policy_value_net_tensorflow import PolicyValueNet
from brain.mcts_pure import MCTSPlayer as MCTS_Pure
from brain.mcts_alphaZero import MCTSPlayer
import pickle

class Human(object):
    """
    human player
    """

    def __init__(self):
        self.player = None
    
    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        try:
            location = take_input()
            if isinstance(location, str):
                location = [int(n, 10) for n in location.split(",")]  # for python3
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            print("invalid move")
            move = self.get_action(board)
        return move

    def __str__(self):
        return "Human {}".format(self.player)


def run():
    n = 5
    width, height = 9, 9
    model_file = 'best_policy.model'
    try:
        board = Board(width=width, height=height, n_in_row=n)
        game = Game(board)
        best_policy = PolicyValueNet(width, height, model_file)
        mcts_player = MCTSPlayer(best_policy.policy_value_fn, c_puct=5, n_playout=1000)
        # human player, input your move in the format: 2,3
        human = Human()
        # set start_player=0 for human first
        game.start_play(human, mcts_player, start_player=1, is_shown=1)
    except KeyboardInterrupt:
        print('\n\rquit')