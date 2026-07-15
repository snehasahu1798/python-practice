x = 100

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

# __name__ and __main__ method
def f1():
    if __name__ == '__main__':
        print("This code executed as a program")
    else:
        print("This code executed as a module")

print(f1())
