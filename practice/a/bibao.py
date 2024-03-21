#编写闭包举例
#闭包可以保存当前的运行环境，
# 以一个类似棋盘游戏的例子来说明。假设棋盘大小为50*50，左上角为坐标系原点(0,0)，
# 我需要一个函数，接收2个参数，分别为方向(direction)，步长(step)，该函数控制棋子的运动。
# 这里需要说明的是，每次运动的起点都是上次运动结束的终点。

#注意：闭包无法改变外部函数局部变量指向的内存地址，但是可以修改值

def startX(x):
    def add(y):
        return x+y;
    return add

def main():
    add = startX(1)
    print("function:",add)
    print("value:",add(2))
if __name__ == '__main__':
    main()