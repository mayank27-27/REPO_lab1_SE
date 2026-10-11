SIZE = 8


def simple_move(board, player, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]

    # Kings can move in both directions
    if piece == player + "K":
        return (
            board[er][ec] == "." and
            abs(er - sr) == 1 and
            abs(ec - sc) == 1
        )

    # Normal pieces move forward only
    direction = -1 if player == "R" else 1

    return (
        board[er][ec] == "." and
        abs(er - sr) == 1 and
        abs(ec - sc) == 1 and
        er - sr == direction
    )


def capture_move(board, player, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]

    mr, mc = (sr + er) // 2, (sc + ec) // 2

    # Basic two-square diagonal capture requirements
    if board[er][ec] != ".":
        return False

    if abs(er - sr) != 2 or abs(ec - sc) != 2:
        return False

    # The jumped piece must belong to the opponent
    if board[mr][mc] in (".", player, player + "K"):
        return False

    # Kings can capture in both directions
    if piece == player + "K":
        return True

    # Normal pieces can capture forward only
    direction = -1 if player == "R" else 1
    return er - sr == 2 * direction


def promote(board):
    for c in range(SIZE):
        if board[0][c] == "R":
            board[0][c] = "RK"
        if board[SIZE - 1][c] == "B":
            board[SIZE - 1][c] = "BK"
