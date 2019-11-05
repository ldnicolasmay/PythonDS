# Python DS
# 1.12 Defining Functions


import string
import random


def square(n):
    return n**2


square(3)
square(square(3))


def square_root(n):
    root = n/2

    for k in range(20):
        root = (1/2) * (root + (n/root))

    return root


square_root(9)
square_root(4563)

letters = string.ascii_lowercase + ' '
letters

random.choices(letters)


def gen_string():
    return ''.join(random.choices(letters, k=28))
    # return ''.join(random.choices(letters, k=4))


def match_string(str):
    if str == "methinks it is like a weasel":
    # if str == "this":
        return True
    return False


def loop_till_match():
    counter = 0
    phrase = gen_string()
    print("%d : %s" % (counter, phrase))
    while not match_string(phrase):
        counter = counter + 1
        phrase = gen_string()
        print("%d : %s" % (counter, phrase))





gen_string()
match_string(gen_string())
loop_till_match()

