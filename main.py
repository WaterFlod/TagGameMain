# Функция с главной логикой игры
def game_logic(game_board, win_board, empty_cell = "   "):
    if game_board == win_board: # Проверка на победный сценарий
        clear_desk()
        print("Победа")
        return  # Выходим из функции, если доски совпали
    else:   # Ищем пустую клетку для передачи её в movement
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