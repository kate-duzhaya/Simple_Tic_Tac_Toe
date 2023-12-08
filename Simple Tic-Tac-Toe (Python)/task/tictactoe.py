from itertools import cycle


def print_grid(grid):
    print("-" * 9)
    for row in grid:
        print("| " + " ".join(row) + " |")
    print("-" * 9)


def define_game_state(grid, x, o):
    game_state = ""
    winner = ""
    # looking for a winner in rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != "_":
            game_state = "Finished"
            winner = grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != "_":
            winner = grid[0][i]
            game_state = "Finished"
    # looking for a winner in diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != "_":
        winner = grid[0][0]
        game_state = "Finished"
    if grid[0][2] == grid[1][1] == grid[2][0] != "_":
        winner = grid[0][2]
        game_state = "Finished"
    # counting X and O
    for i in range(3):
        for j in range(3):
            if grid[i][j].upper() == "X":
                x += 1
            if grid[i][j].upper() == "O":
                o += 1
    if x + o == 9 and not winner:
        game_state = "Draw"

    return game_state, winner


def check_user_move():
    while True:
        try:
            user_cell = input().split()
            coordinates = [int(i) for i in user_cell]
            valid_numbers = all(1 <= c <= 3 for c in coordinates)
            if not valid_numbers:
                print("Coordinates should be from 1 to 3!")
                continue
            if new_grid[coordinates[0] - 1][coordinates[1] - 1].upper() in "XO":
                print("This cell is occupied! Choose another one!")
            else:
                new_grid[coordinates[0] - 1][coordinates[1] - 1] = next(moves_iterator)
                break
        except ValueError:
            print("You should enter numbers!")


new_grid = [['_' for _ in range(3)] for _ in range(3)]
moves = ["X", "O"]
moves_iterator = cycle(moves)
x_count = 0
o_count = 0
while True:
    print_grid(new_grid)
    check_user_move()
    define_game_state(new_grid, x_count, o_count)
    if define_game_state(new_grid, x_count, o_count)[0] == "Draw":
        print_grid(new_grid)
        print("Draw")
        break
    if define_game_state(new_grid, x_count, o_count)[0] == "Finished":
        print_grid(new_grid)
        print(f"{define_game_state(new_grid, x_count, o_count)[1]} wins")
        break
