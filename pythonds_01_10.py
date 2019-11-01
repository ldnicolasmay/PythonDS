# Python DS
# 1.10 Control Structures


# Iteration

# while

counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

for item in [1,3,6,2,5]:
    print(item)

for item in range(5):
    print(item ** 2)

# for

wordlist = ["cat", "dog", "rabbit"]
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)


# Selection Statements

score = 73
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

wordlist = ["cat", "dog", "rabbit"]
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)


# List Comprehensions

sqlist = []
for x in range(1, 11):
    sqlist.append(x * x)
sqlist

sqlist = [x * x for x in range(1, 11)]
sqlist

sqlist = [x * x for x in range(1, 11) if x % 2 != 0]
sqlist


def is_odd(n):
    return not n % 2 == 0

def is_even(n):
    return n % 2 == 0


sqlist = [x * x for x in range(1, 11) if is_odd(x)]
sqlist

sqlist = [x * x for x in range(1, 11) if is_even(x)]
sqlist

[ch.upper() for ch in "comprehension" if ch not in "aeiou"]

wordlist = ["cat", "dog", "rabbit"]
letterlist = []
[[letterlist.append(c) for c in w] for w in wordlist]
print(letterlist)

wordlist = ["cat", "dog", "rabbit"]
letterlist = []
[[letterlist.append(c) for c in w if c not in letterlist] for w in wordlist]
print(letterlist)

