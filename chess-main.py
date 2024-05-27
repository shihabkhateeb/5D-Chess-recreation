import chess
import chess.svg

board = chess.Board()

board_states = []
board_moves = ["e2e4", "e7e5", "d1h5"]

#Original board state with no moves is recorded.
board_states.append(board.fen())

#Moves are made in succession, board state is recorded after each move.
for move in board_moves:
    board.push_uci(move)
    board_states.append(board.fen())

#Illegal move made, by adding a queen to a board with a preexisting queen.
board.set_piece_at(chess.F7, chess.Piece(chess.QUEEN, chess.WHITE))
board_states.append(board.fen())

#Confirmation of functionality of time axis, illegal axis.
for state in board_states:
    board = chess.Board(state)
    print(board)
    print("\n")
