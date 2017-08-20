'''
[
    [0,0,0,1,-1....],
    [{'name': 'bot1', 'life': 10, 'history': ['go_up'....]}, 0,-1,0...]
    ......
]

0 - пустая клетка
1 - монетка
-1 - стена
{...} - бот



........
.#..*...
........
........

'''
import random


def make_choice(x, y, field):
    width = len(field)
    height = len(field[0])

    # от нас до левого края
    for i in range(x - 1, -1, -1):
        if field[i][y] in [1, -1, 0]:
            continue
        # если попали сюда - в клетке кто то есть
        if field[i][y]['life'] <= field[x][y]['life']:
            return "fire_left"
        else:
            return random.choice(['go_up', 'go_down'])

    for i in range(x + 1, width):
        if field[i][y] in [1, -1, 0]:
            continue
        if field[i][y]['life'] <= field[x][y]['life']:
            return "fire_right"
        else:
            return random.choice(['go_up', 'go_down'])

    for i in range(y + 1, height):
        if field[x][i] in [1, -1, 0]:
            continue
        if field[x][i]['life'] <= field[x][y]['life']:
            return "fire_down"
        else:
            return random.choice(['go_left', 'go_right'])

    for i in range(y - 1, -1, -1):
        if field[x][i] in [1, -1, 0]:
            continue
        if field[x][i]['life'] <= field[x][y]['life']:
            return "fire_up"
        else:
            return random.choice(['go_left', 'go_right'])

    return random.choice([
        "go_right", "go_left",
        "go_down", "go_up"
    ])