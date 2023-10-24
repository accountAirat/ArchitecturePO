from random import choice
import GoldGenerator, GemGenerator

fabric_list = []

fabric_list.append(GoldGenerator())
fabric_list.append(GemGenerator())

for i in range(20):
    fabric = choice(fabric_list).create_item()
    fabric.open()
