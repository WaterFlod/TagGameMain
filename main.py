import random


# Функция с главной логикой игры
def game_logic(game_board, win_board, empty_cell = "   "):
    # Проверка на победный сценарий
    if game_board == win_board:
        clear_desk()
        print("Победа")
        return  # Выходим из функции, если доски совпали
    # Ищем пустую клетку для передачи её в movement
    else:  
        clear_desk()
        print_board(game_board)

        for x in range(len(game_board)):
            for y in range(len(game_board[x])):
                if game_board[x][y] == empty_cell:
                    x_empty = x  # Столбец
                    y_empty = y  # Строка
                    break

    move = input("Куда двигаемся? W A S D: \n").lower()  # Ждём ход пользователя
    
    if move in ("w", "a", "s", "d"):
        movement(move, x_empty, y_empty)
    else:
        text("Нет такого направления")
        game_logic(game_board)


# Перемешивает доску
def random_desk(game_board, x, y):
    for _ in range(50):
        move = list()  # Переменная принимающая возможные движения

        if x > 0: move.append("w")
        if x < 3: move.append("s")
        if y > 0: move.append("a")
        if y < 3: move.append("d")

        move = random.choice(move)
        
        if move == "w":
            game_board[x][y], game_board[x-1][y] = game_board[x-1][y], game_board[x][y]
            x -= 1
        elif move == "s":
            game_board[x][y], game_board[x+1][y] = game_board[x+1][y], game_board[x][y]
            x += 1
        elif move == "a":
            game_board[x][y], game_board[x][y-1] = game_board[x][y-1], game_board[x][y]
            y -= 1
        elif move == "d":
            game_board[x][y], game_board[x][y+1] = game_board[x][y+1], game_board[x][y]
            y += 1