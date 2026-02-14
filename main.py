import colorama
import random

ch = int(input("введите 1/2"))
ran = random.randint(1, 2)

if ch == ran:
    print("вы проиграли")
else:
    print("вы победили")