from test6 import roll_dice
#什么是yield，yield的作用
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)


def bar():
    roll_dice(2)

if __name__ == '__main__':
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))

    bar()