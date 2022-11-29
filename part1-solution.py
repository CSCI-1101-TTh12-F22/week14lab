def myfunction(a="pardner", b=1, c=False):
    if c == True:
        b += 1
    for i in range(b):
        print("Howdy, " + a + "!")

# Task 1
# What does this print out?
myfunction("Herbert", 4, False)


# Task 2
# Fix this function call so that it works with the current definition.
myfunction(b=2, c=True, a="Marjorie")


# Task 3
# Fix the function definition so that this function call prints out
# Howdy, pardner!
myfunction()

    


