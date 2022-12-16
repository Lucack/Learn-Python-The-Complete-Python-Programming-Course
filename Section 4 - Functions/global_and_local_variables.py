total = 10 #its a global variable

def multply(num1, num2):
    total = num1 * num2 # total is a local variable
    return total

print(multply(10,5))

print(total)
