import random

## ABSOLUTE VALUE
mylist = [random.randint(-10,10) for i in range(5)]
print(mylist)

# for loop
list1 = []
for i in mylist:
    list1.append(abs(i))


# list comprehension
list2 = [abs(i) for i in mylist]


# map()
list3 = list(map(abs, mylist))


# map() and lambda (no abs())
list4 = list(map(lambda x: -x if x < 0 else x, mylist))

print(list1, list2, list3, list4, sep="\n")


## SQUARE ROOT
import math
mylist = [9, 25, 16, 64]

# for loop
list1 = []
for i in mylist:
    list1.append(math.sqrt(i))

# list comprehension
list2 = [math.sqrt(i) for i in mylist]

# map()
list3 = list(map(math.sqrt, mylist))

# map() and lambda (no sqrt())
list4 = list(map(lambda x: x**(1/2), mylist))

print(list1, list2, list3, list4, sep="\n")

## SWAP CASE
mylist = ["Boston College", "FedEx", "piano", "NFL"]

# for loop
list1 = []
for i in mylist:
    list1.append(i.swapcase())

# list comprehension
list2 = [s.swapcase() for s in mylist]

# map()
list3 = list(map(str.swapcase, mylist))

# map() and lambda (no swapcase())
# Not really supposed to (allowed to?) use a for loop in a lambda function
# Can you make it work?

print(list1, list2, list3, sep="\n")


