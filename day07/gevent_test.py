import gevent


def foo(a, b):
    print("running foo...", a, b)
    gevent.sleep(2)
    print("foo again")


def bar():
    print("running bar...")
    gevent.sleep(3)
    print('bar again')


# 将函数封装为协程，遇到gevent阻塞自动执行
f = gevent.spawn(foo, 1, 'hello')
g = gevent.spawn(bar)
gevent.joinall([f, g])
