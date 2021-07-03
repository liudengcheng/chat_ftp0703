from greenlet import greenlet


def test1():
    print("begin test1")
    gr2.switch()
    print("finish test1")
    gr2.switch()


def test2():
    print("begin test2")
    gr1.switch()
    print("finish test2")


# 将两个函数变成协程函数
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()