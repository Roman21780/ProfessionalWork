def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        return "корней нет"
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (round(x1, 2), round(x2, 2))
    else:
        return round(-b / (2 * a), 2)


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
