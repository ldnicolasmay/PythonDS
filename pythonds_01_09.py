# Python DS
# 1.9 Input and Output

aName = input("Enter name: ")

print("Your name in call capitals is"
      , aName.upper()
      , "and has length"
      , len(aName)
      )

sradius = input("Circle radius: ")
radius = float(sradius)
diameter = 2 * radius
print(diameter)

print("Hello")
print("Hello", "world")
print("Hello", "world", sep="***")
print("Hello", "world", end="***")
print("Hello", "cruel", "world", sep="-->")

age = 21
print(aName, "is", age, "years old.")
print("%s is %d years old." % (aName, age))

price = 24
item = "banana"
print("The %s costs %d cents" % (item, price))
print("The %+10s costs %5.2f cents" % (item, price))
print("The %+10s costs %10.2f cents" % (item, price))
itemdict = {"item": "banana", "cost": 24}
print("The %(item)s costs %(cost)7.1f cents" % itemdict)

