# Given an integer n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

#Input Format

# A single line containing a positive integer

#Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

def returnWeird(n):
    if n%2 is not 0:
        print("Weird")
    if n%2 == 0 and n in range(2,6):
        print("Not Weird")
    if n%2 == 0 and n in range(6,21):
        print(n)
        print("Weird")
    if n%2 == 0 and n > 20:
        print("Not Weird")


myNum = 20
returnWeird(myNum)


