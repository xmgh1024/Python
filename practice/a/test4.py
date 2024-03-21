"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""
def f():
    x = float(input("请输入一个数："))
    if x>1:
        return 3*x - 5
    elif x>=-1:
        return x + 2
    else:
        return 5*x + 3


if __name__ == '__main__':
    value = f()
    print(value)
