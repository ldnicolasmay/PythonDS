# PythonDS
# 1.8 Getting Started with Data

print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 10)
print(6 / 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(3 / 6)
print(3 // 6)
print(3 % 6)
print(2 ** 100)

True
False
False or True
not (False or True)
True and True

print(5 == 10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))


# Assignment

theSum = 0
# theSum: int = 0
theSum
theSum = theSum + 1
theSum
theSum = True
# theSum: bool = True
theSum


# Lists

[1,3,True,6.5]
myList = [1, 3, True, 6.5]
myList

myList[0]
myList + ['a', 'hey']
myList * 3
3 in myList
5 in myList
len(myList)
myList[1:3]

myList = [1, 2, 3, 4]
A = [myList] * 3
print(A)
myList[2] = 45
print(A)

myList = [1, 2, 3, 4]
print(myList)

myList.append(5)
print(myList)

myList.insert(0, 0)
print(myList)

lastInList = myList.pop()
print(lastInList)
print(myList)

myList.reverse()
print(myList)

myList.sort()
print(myList)

del myList[2]
print(myList)

print(myList.index(2))
print(myList.index(1))

print(myList.count(2))
print(myList.count(0))

myList.remove(0)
print(myList)


# dot notation on class objects

(54).__add__(21)


# Ranges

range(10)
list(range(10))
range(5, 10)
list(range(5, 10))
list(range(5, 10, 2))
list(range(10, 1, -1))


# Strings

"Nicolas"
myName = "Nicolas"
myName[3]
myName * 2
len(myName)

myName.upper()
print(myName)

myName.center(11)
myName.center(80 - len(myName))
print(myName.center(80 - len(myName)))

myName.find('c')

myName.split('o')

myName.count('n')
myName.count('N')

myName.ljust(20)

myName.lower()

myName.rjust(20)


# Mutability

# Lists are mutable.
# Strings are immutable.
# Tuples are immutable.

# Tuples

myTuple = (2, True, 4.96)
print(myTuple)

len(myTuple)

myTuple[0]

myTuple * 3

myTuple[0:2]

myTuple[1] = False # throws error b/c tuples are immutable


# Sets

{3, 6, "cat", 4.5, False}

mySet = {3, 6, "cat", 4.5, False}
mySet

3 in mySet
4 in mySet

mySet | {3, 4, 5, 6}  # set union
mySet & {3, 4, 5, 6}  # set intersection
mySet - {3, 4, 5, 6}  # set difference

mySet <= {3, 4, 5, 6}  # issubset => False
mySet <= {3, 6, "cat", 4.5, False, "bazingas"}  # issubset => True

mySet.union({3, 4, 5, 6})
mySet.intersection({3, 4, 5, 6})
mySet.difference({3, 4, 5, 6})

mySet.issubset({3, 4, 5, 6})
mySet.issubset({3, 6, "cat", 4.5, False, "bazingas"})

mySet.add(True)
mySet

mySet.remove(True)
mySet

myPop = mySet.pop()
myPop
mySet

mySet.clear()
mySet


# Dictionaries

capitals = {"Iowa":"DesMoines", "Wisconsin":"Madison"}

print(capitals["Iowa"])

capitals["Utah"] = "Salt Lake City"
print(capitals)

capitals["California"] = "Sacramento"

print(len(capitals))

for k in capitals:
    print(capitals[k], "is the capital of", k)

for k, v in capitals.items():
    print(v, "is the capital of", k)

"California" in capitals
"Michigan" in capitals

capitals["Michigan"] = "Lansing"
for k, v in capitals.items():
    print(v, "is the capital of", k)

del capitals["Michigan"]
capitals

capitals.keys()
capitals.values()
capitals.items()
capitals.get("Utah")
capitals.get("Arizona")
capitals.get("Arizona", "Utah")
