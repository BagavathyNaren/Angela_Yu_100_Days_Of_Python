import math
import sys

def print_board(board):
    """Prints the 3x3 board."""
    print("\n")
    for r in range(3):
        row = " | ".join(board[r])
        print(" " + row)
        if r < 2:
            print("---+---+---")
    print("\n")

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def available_moves(board):
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                moves.append((r, c))
    return moves

def check_winner(board):
    """Return 'X' or 'O' if There's a winner, 'Draw' if full, or None otherwise."""
    lines = []
    # Rows and cols
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])  # row
        lines.append([board[0][i], board[1][i], board[2][i]])  # col
    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != " " and line.count(line[0]) == 3:
            return line[0]

    if all(cell != " " for row in board for cell in row):
        return "Draw"
    return None

def minimax(board, depth, is_maximizing, ai_player, human_player, alpha=-math.inf, beta=math.inf):
    """
    Minimax with alpha-beta pruning.
    Returns (score, move) where move is (r,c) or None.
    Scores: win for ai -> 10 - depth, loss -> depth - 10, draw -> 0
    Depth used to prefer faster wins and delay losses.
    """
    winner = check_winner(board)
    if winner == ai_player:
        return 10 - depth, None
    elif winner == human_player:
        return depth - 10, None
    elif winner == "Draw":
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for (r, c) in available_moves(board):
            board[r][c] = ai_player
            score, _ = minimax(board, depth + 1, False, ai_player, human_player, alpha, beta)
            board[r][c] = " "
            if score > best_score:
                best_score = score
                best_move = (r, c)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # beta cut-off
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for (r, c) in available_moves(board):
            board[r][c] = human_player
            score, _ = minimax(board, depth + 1, True, ai_player, human_player, alpha, beta)
            board[r][c] = " "
            if score < best_score:
                best_score = score
                best_move = (r, c)
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # alpha cut-off
        return best_score, best_move

def get_human_move(board):
    while True:
        try:
            move = input("Enter your move (row,col) where row and col are 1-3 (e.g. 2,3): ").strip()
            if move.lower() in ("q", "quit", "exit"):
                print("Quitting game.")
                sys.exit(0)
            r, c = map(int, move.split(","))
            if r not in (1, 2, 3) or c not in (1, 2, 3):
                print("Coordinates must be 1, 2 or 3.")
                continue
            r -= 1; c -= 1
            if board[r][c] != " ":
                print("That cell is already taken.")
                continue
            return r, c
        except ValueError:
            print("Bad input format. Use row,col (example: 1,3).")

def ai_move(board, ai_player, human_player):
    _, move = minimax(board, depth=0, is_maximizing=True, ai_player=ai_player, human_player=human_player)
    # move should never be None here (unless board full)
    if move:
        return move
    # fallback (shouldn't be reached)
    moves = available_moves(board)
    return moves[0] if moves else None

def choose_symbol():
    while True:
        choice = input("Choose your symbol: X (goes first) or O (goes second) [X/O]: ").strip().upper()
        if choice in ("X", "O"):
            return choice
        print("Pick X or O.")

def main():
    print("Tic Tac Toe — Unbeatable AI (minimax + alpha-beta)\n")
    human = choose_symbol()
    ai = "O" if human == "X" else "X"
    current = "X"  # X always starts
    board = create_board()

    print(f"You are '{human}'. AI is '{ai}'.")
    print("Enter moves like: 1,3  (row 1, column 3). Type 'q' to quit.\n")

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw.")
            else:
                print(f"Player '{winner}' wins!")
            break

        if current == human:
            r, c = get_human_move(board)
            board[r][c] = human
        else:
            print("AI is thinking...")
            mv = ai_move(board, ai, human)
            if mv:
                board[mv[0]][mv[1]] = ai
                print(f"AI plays at {mv[0]+1},{mv[1]+1}")
            else:
                # no moves left (should be handled by winner check)
                pass

        current = ai if current == human else human

if __name__ == "__main__":
    main()