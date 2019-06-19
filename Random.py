import random

random_number = random.random() # sinh ra 1 số float bất kỳ
print(random_number)

from random import SystemRandom
crypto = SystemRandom() # tạo ra 1 float trong khoảng [0,1]
print(crypto.random())


