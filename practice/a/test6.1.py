#计算8个苹果分给4个小朋友，每个小朋友至少分一个，有几种分法？
#解析：采用插板法。8个苹果之间有7个空隙，插入3个插板即可分成4组，每组对应一个小朋友

#计算n的阶乘 n!
def f(n):
    result = 1
    for a in range(1,n+1):
        result*=a
    return result

if __name__ == '__main__':
    a = f(3)
    print(a)
    m = int(input("请输入m："))
    n = int(input("请输入n："))
    l = f(m)//f(n)//f(m-n)
    # 双斜杠的含义与单斜杠含义的区别在于，前者会向下取整，后者不会。后者会正常进行除法运算
    print(l)