def test00(a, b, c):
    print("%.2f" % a)
    print("%.2f" % b)
    print("%.2f" % c)


def test01(a, b, c):
    print('{:.2f}'.format(a))
    print('{:.2f}'.format(b))
    print('{:.2f}'.format(c))

def test02():
    a = 0.3051
    b = 0.315
    c = 0.305
    print('{:.2f}'.format(a))
    print('{:.2f}'.format(b))
    print('{:.2f}'.format(c))

if __name__ == '__main__':
    a = 0.3051
    b = 0.315
    c = 0.305
    test00(a, b, c)
    test01(a, b, c)

    # test02()