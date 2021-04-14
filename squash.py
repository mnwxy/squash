#We assume that input is between -range and +range.
def squashA(input, range=100):
    debugging = False
    shiftedInput = input+range+1 #making the input greater than 1
    squashedInput = 1/(shiftedInput+0.0) #squashing the input to be between 0 and 1; we convert to a float
    flippedSquashedInput = 1-squashedInput #flipping the order of the input to preserve the strict order
    if debugging:
        print("shiftedInput: " + str(shiftedInput))
        print("squashedInput: " + str(squashedInput))
        print("flippedSquashedInput: " + str(flippedSquashedInput))
    return flippedSquashedInput

def squashB(input):
    if input < 0:
        shiftedInput = input-1 #we need to make the input less than 1 so that we can divide by it
        squashedInput = 1/(shiftedInput+0.0) #squashing the input to be between -1 and 0; we convert denominator to a float
        flippedSquashedInput = -squashedInput #we have to flip the input both to make it positive and to preserve the strict order
    else:
        shiftedInput = input+1
        squashedInput = 1/(shiftedInput + 0.0)
        flippedSquashedInput = 3-squashedInput #we subtract from 3 so that it's in a different position from the negatives
    return flippedSquashedInput

print("squashA tests")
print(squashA(-50))
print(squashA(5))
print(squashA(6))
print(squashA(4757643))
print("squashB tests")
print(squashB(-183))
print(squashB(5))
print(squashB(6))
print(squashB(4757277385))
