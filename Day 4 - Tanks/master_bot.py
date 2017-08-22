import random


def check_money(x, y, field):

    width = len(field)
    height = len(field[0])

    money_right = 1000
    money_left = 1000
    money_top = 1000
    money_bottom = 1000

    for i in range(x - 1, -1, -1):
        if field[i][y] == -1:
            break
        if field[i][y] == 1:
            money_left = abs(x-i)

    for i in range(x + 1, width):
        if field[i][y] == -1:
            break
        if field[i][y] == 1:
            money_right = abs(x-i)

    for i in range(y + 1, height):
        if field[x][i] == -1:
            break
        if field[x][i] == 1:
            money_bottom = abs(y-i)

    for i in range(y - 1, -1, -1):
        if field[x][i] == -1:
            break
        if field[x][i] == 1:
            money_top = abs(y-i)

    if money_top == min([money_top, money_bottom, money_left, money_right]):
        return "go_up"
    if money_bottom == min([money_top, money_bottom, money_left, money_right]):
        return "go_bottom"
    if money_left == min([money_top, money_bottom, money_left, money_right]):
        return "go_left"
    if money_right == min([money_top, money_bottom, money_left, money_right]):
        return "go_right"

    return False


def check_battle(x, y, field):
    width = len(field)
    height = len(field[0])

    enemy_left = False
    enemy_right = False
    enemy_top = False
    enemy_bottom = False

    for i in range(x - 1, -1, -1):
        if field[i][y] == -1:
            break
        if field[i][y] not in [0, 1]:
            enemy_left = field[i][y]['life']
            if field[i][y]['history'] != [] and field[i][y]['history'][-1] in ['error', 'crash']:
                return 'fire_left'

    for i in range(x + 1, width):
        if field[i][y] == -1:
            break
        if field[i][y] not in [0, 1]:
            enemy_right = field[i][y]['life']
            if field[i][y]['history'] != [] and field[i][y]['history'][-1] in ['error', 'crash']:
                return 'fire_right'

    for i in range(y + 1, height):
        if field[x][i] == -1:
            break
        if field[x][i] not in [0, 1]:
            enemy_bottom = field[x][i]['life']
            if field[x][i]['history'] != [] and field[x][i]['history'][-1] in ['error', 'crash']:
                return 'fire_bottom'

    for i in range(y - 1, -1, -1):
        if field[x][i] == -1:
            break
        if field[x][i] not in [0, 1]:
            enemy_top = field[x][i]['life']
            if field[x][i]['history'] != [] and field[x][i]['history'][-1] in ['error', 'crash']:
                return 'fire_up'
    print ([enemy_left, enemy_right, enemy_bottom, enemy_top])

    if int(enemy_bottom) + int(enemy_top) + int(enemy_right) + int(enemy_left) >= field[x][y]['life']:
        if not enemy_top and not enemy_bottom:
            if y > 0 and field[x][y - 1] != -1:
                return "go_up"
            if y < height - 1 and field[x][y + 1] != -1:
                return "go_down"
            return random.choice(["go_left", "go_right"])
        if not enemy_left and not enemy_right:
            if x > 0 and field[x - 1][y] != -1:
                return "go_left"
            if x < width - 1 and field[x + 1][y] != -1:
                return "go_right"
            return random.choice(["go_up", "go_down"])
        return random.choice(["go_up", "go_down", "go_left", "go_right"])
    if enemy_left:
        return "fire_left"
    if enemy_top:
        return "fire_up"
    if enemy_bottom:
        return "fire_bottom"
    if enemy_right:
        return "fire_right"
    return False


def make_choice(x, y, field):
    result = check_battle(x, y, field)
    if result != False:
        return result

    result = check_money(x, y, field)
    if result != False:
        return result

    return random.choice(["go_up", "go_down", "go_left", "go_right"])
