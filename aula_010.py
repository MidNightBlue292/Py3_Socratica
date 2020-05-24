import random


def random_walk(n):
    x = y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return (x, y)


for i in range(25):
    walk = random_walk(10)
    print(walk, 'Distância de casa:', abs(walk[0]) + abs(walk[1]))
