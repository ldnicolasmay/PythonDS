
import random

def generate_one(strlen):

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res


# print(generate_one(28))


def generate_one_2(cur_string, goal_string):

    goal_len = len(goal_string)
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""

    for i in range(goal_len):
        if cur_string[i] == goal_string[i]:
            res = res + cur_string[i]
        else:
            res = res + alphabet[random.randrange(27)]

    return res


generate_one_2("methinks it is like a weasel", "methinks it is like a weasel")
generate_one_2("methinks it is like a aaaaaa", "methinks it is like a weasel")


def score(goal, teststring):

    goal_len = len(goal)
    num_same = 0
    for i in range(goal_len):
        if goal[i] == teststring[i]:
            num_same = num_same + 1

    return num_same / goal_len


# print(score("methinks it is like a weasel", generate_one(28)))


def main():

    goal_string = "methinks it is like a weasel"
    new_string = generate_one(28)
    new_string = generate_one_2(new_string, goal_string)
    best = 0.0
    new_score = score(goal_string, new_string)

    while new_score < 1.0:
        if new_score > best:
            print("%s : %f" % (new_string, new_score))
            best = new_score
        new_string = generate_one_2(new_string, goal_string)
        new_score = score(goal_string, new_string)

main()
