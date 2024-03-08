from random import randint


def roll_dice(n):
    """
    摇色子

    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for a in range(n):
        print(a)
        total += randint(1, 6)
        print(total)
    for a in range(n):
        print(a)
        print(total)
    return total


if __name__ == '__main__':
    num= roll_dice(2)
    print(num)

