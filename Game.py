name1 = input("Введите имя первого игрока: ")
name2 = input("Введите имя второго игрока: ")
print()
print(f"                                              {name1} и {name2}!")
print()
print("                                             Добро пожаловать ")
print("                                                  в игру")
print("                                              Крестики-нолики")
print(f'{name1} ходит "Х" {name2} ходит "0"')

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]


victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = f"{name1}"

        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = f"{name2}"

    return win


game_over = False
player1 = True

while game_over == False:
    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input(f"{name1}, ваш ход: "))
        if step >= 10 or step <= 0:
            print("вы вышли за диапазон")
            continue
        if step not in maps:
            print("данное значение уже занято")
            continue


    else:
        symbol = "O"
        step = int(input(f"{name2}, ваш ход: "))
        if step >= 10 or step <= 0:
            print("вы вышли за диапазон")
            continue
        if step not in maps:
            print("данное значение уже занято")
            continue


    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_maps()
print("Победил", win)