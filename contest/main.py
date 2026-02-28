def create_phone_number(number):
    """Решение для Задачи 1"""
    return f'({number[0]}{number[1]}{number[2]}) {number[3]}{number[4]}{number[5]}-{number[6]}{number[7]}{number[8]}{number[9]}'

def duplicate_encode(text: str) -> str:
    """Решение для Задачи 2"""
    result = ''
    text_lower = text.lower()
    for symbol in text:
        if text_lower.count(symbol) == 1:
            result += '('
        else:
            result += ')'
    return result

def is_valid_walk(walk: list) -> bool:
    """Решение для Задачи 3"""
    west_east = 0
    north_south = 0
    if len(walk) != 10:
        return False
    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'w':
            west_east -= 1
        elif direction == 'e':
            west_east += 1
    if west_east == 0 and north_south == 0:
        return True
    else:
        return False
def move_zeros(lst: list) -> list:
    """Решение для Задачи 4"""
    result = []
    zeros = []
    for i in lst:
        if i != 0:
            result.append(i)
        else:
                zeros.append(0)
    return result + zeros

def find_uniq(lst: list):
    """Решение для Задачи 5"""
    unique = set(lst)
    for number in unique:
        if lst.count(number) == 1:
            return number
