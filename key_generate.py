from itertools import permutations
from random import choice


interval = [num for num in range(9,20)]
elements = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

keys = []



for string in permutations(elements,4):
    num_cont = []
    for letter in string:
        num_cont.append(int(str(letter),36))
    if sum(num_cont)/4 in interval:
        keys.append(string)


def key():
    print(
        "".join(choice(keys))+"-\n"+ 
          "".join(choice(keys))+"-"+ "".join(choice(keys))
          )
    



