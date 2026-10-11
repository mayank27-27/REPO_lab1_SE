from board import initial_board, move_piece, SIZE
from rules import simple_move, capture_move, promote


class Checkers:
    def __init__(self):
        self.board = initial_board()
        self.player = "R"

    def print_board(self):
        print("\n   " + " ".join(str(c) for c in range(SIZE)))
        for r, row in enumerate(self.board):
            print(f"{r}  " + " ".join(row))

    def has_legal_move(self, player):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.board[r][c] not in (player, player + "K"):
                    continue

                start = (r, c)

                for er in range(SIZE):
                    for ec in range(SIZE):
                        end = (er, ec)

                        if capture_move(self.board, player, start, end):
                            return True

                        if simple_move(self.board, player, start, end):
                            return True

        return False
    def has_capture(self, player):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.board[r][c] not in (player, player + "K"):
                    continue

                start = (r, c)

                for er in range(SIZE):
                    for ec in range(SIZE):
                        end = (er, ec)

                        if capture_move(self.board, player, start, end):
                            return True

        return False
    def has_capture_from(self, player, start):
        sr, sc = start

        for er in range(SIZE):
            for ec in range(SIZE):
                end = (er, ec)

                if capture_move(self.board, player, start, end):
                    return True

        return False
    def announce_move(self, player, start, end, capture=False):
        action = "captures" if capture else "moves"
        print(f"{player}: {start} {action} {end}")

    def run(self):
        print("Checkers — move: sr sc er ec")
        while True:
            self.print_board()

            if not any(
                piece in (self.player, self.player + "K")
                for row in self.board
                for piece in row
            ):
                winner = "B" if self.player == "R" else "R"
                print(f"{winner} wins! {self.player} has no pieces left.")
                return

            if not self.has_legal_move(self.player):
                winner = "B" if self.player == "R" else "R"
                print(f"{winner} wins! {self.player} has no legal moves.")
                return

            raw = input(f"{self.player}> ").strip().lower().split()
            if raw == ["q"]:
                return
            if len(raw) != 4:
                print("Enter four coordinates.")
                continue
            try:
                sr, sc, er, ec = map(int, raw)
            except ValueError:
                print("Coordinates must be numbers.")
                continue
            if not all(0 <= x < SIZE for x in (sr, sc, er, ec)):
                print("Outside board.")
                continue
            if self.board[sr][sc] not in (self.player, self.player + "K"):
                print("That is not your piece.")
                continue

            start, end = (sr, sc), (er, ec)

            # Check whether the player has any capture available
            forced_capture = self.has_capture(self.player)

            if forced_capture and not capture_move(
                self.board, self.player, start, end
            ):
                print("You must capture when a capture is available.")
                continue

            if capture_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)

                # Remove the jumped opponent piece
                mr = (sr + er) // 2
                mc = (sc + ec) // 2
                self.board[mr][mc] = "."

                self.announce_move(self.player, start, end, capture=True)

                # Check for another capture with the same piece
                while self.has_capture_from(self.player, end):
                    self.print_board()

                    raw = input(
                        f"{self.player} must continue capturing from "
                        f"{end[0]} {end[1]}> "
                    ).strip().lower().split()

                    if raw == ["q"]:
                        return

                    if len(raw) != 2:
                        print("Enter the destination row and column.")
                        continue

                    try:
                        er, ec = map(int, raw)
                    except ValueError:
                        print("Coordinates must be numbers.")
                        continue

                    if not all(0 <= x < SIZE for x in (er, ec)):
                        print("Outside board.")
                        continue

                    next_end = (er, ec)

                    if not capture_move(
                        self.board, self.player, end, next_end
                    ):
                        print("You must make another capture.")
                        continue

                    move_piece(self.board, end, next_end)

                    # Remove the jumped opponent piece
                    mr = (end[0] + er) // 2
                    mc = (end[1] + ec) // 2
                    self.board[mr][mc] = "."

                    self.announce_move(self.player, end, next_end, capture=True)

                    end = next_end
                    # Promotion ends the current capture sequence
                    if (
                        self.board[end[0]][end[1]] == "R"
                        and end[0] == 0
                    ) or (
                        self.board[end[0]][end[1]] == "B"
                        and end[0] == SIZE - 1
                    ):
                        promote(self.board)
                        break

                promote(self.board)

            elif simple_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)
                self.announce_move(self.player, start, end)

                old_piece = self.board[end[0]][end[1]]
                promote(self.board)

                if self.board[end[0]][end[1]] != old_piece:
                    print(f"{self.player} promotes to king!")

            else:
                print("Invalid move.")
                continue

            promote(self.board)
            self.player = "B" if self.player == "R" else "R"
