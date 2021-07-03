import time
import threading


# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看账户余额
    def get_balance(self):
        return self.balance


# 转账函数
def transfer(from_, to_, amount):
    # 上锁成功返回True
    if from_.lock.acquire():
        from_.withdraw(amount)  # 自己账户金额减少
        if to_.lock.acquire():
            to_.deposit(amount)  # 对方账户金额增加
            to_.lock.release()
        from_.lock.release()  # 自己账户上锁
    print("转账完成")


# 创建两个账户
Abby = Account("Abby", 5000, threading.Lock())
Levi = Account("Levi", 3000, threading.Lock())

t = threading.Thread(target=transfer, args=(Abby, Levi, 1500))
t.start()

t.join()
print("Abby:", Abby.get_balance())
print("Levi:", Levi.get_balance())
