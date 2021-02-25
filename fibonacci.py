def fibonacci(seqNum):
    if seqNum == 1:
        return 0
    elif seqNum == 2 or seqNum == 3:
        return 1
    
    return fibonacci(seqNum-1) + fibonacci(seqNum-2)

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)


