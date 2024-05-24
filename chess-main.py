import chess
import chess.svg

board = chess.Board()

board_states = []
board_moves = ["e2e4", "e7e5", "d1h5"]

for move in board_moves:
    board.push_uci(move)
    board_states.append(board.fen())

for state in board_states:
    print(state)
