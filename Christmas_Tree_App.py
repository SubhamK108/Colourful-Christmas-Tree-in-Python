print('Merry Christmas from SUBHAM KARMAKAR\n\n')


import os
import time
import threading
import random

Tree = list(open(r'Assets/Modified_Tree.txt', 'r').read().rstrip())

lock = threading.Lock()

def ColourPattern(colour):
    list_of_colours = [f'\033[91m█\033[0m', f'\033[92m█\033[0m', f'\033[94m█\033[0m', f'\033[93m█\033[0m']
    if colour == 'Red':
        return f'\033[91m█\033[0m'
    if colour == 'Green':
        return f'\033[92m█\033[0m'
    if colour == 'Blue':
        return f'\033[94m█\033[0m'
    if colour == 'Yellow':
        return f'\033[93m█\033[0m'
    if colour == 'Other':
        return (random.choice(list_of_colours))

def LightUp(colour, indices):
    Off = True
    while True:
        for idx in indices:
            Tree[idx] = ColourPattern(colour) if Off else '█'

            lock.acquire()
            os.system('cls' if os.name == 'nt' else 'clear')

            print(''.join(Tree))
            lock.release()

            Off = not Off
            time.sleep(random.uniform(0.00001, 0.00003))


Red = []
Green = []
Blue = []
Yellow = []
Other = []

for i, c in enumerate(Tree):
    if c == 'R':
        Red.append(i)
        Tree[i] = '█'
    if c == 'G':
        Green.append(i)
        Tree[i] = '█'
    if c == 'B':
        Blue.append(i)
        Tree[i] = '█'
    if c == 'Y':
        Yellow.append(i)
        Tree[i] = '█'
    if c == '$':
        Other.append(i)
        Tree[i] = '█'


Tr = threading.Thread(target=LightUp, args=('Red', Red))
Tg = threading.Thread(target=LightUp, args=('Green', Green))
Tb = threading.Thread(target=LightUp, args=('Blue', Blue))
Ty = threading.Thread(target=LightUp, args=('Yellow', Yellow))
To = threading.Thread(target=LightUp, args=('Other', Other))

for T in [Tr, Tg, Tb, Ty, To]:
    T.start()

for T in [Tr, Tg, Tb, Ty, To]:
    T.join()
