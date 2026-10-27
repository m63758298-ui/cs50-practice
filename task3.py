def main():
    x = int(input("x: "))
    y = int(input("y: "))
    print(f"Sum: {add(x, y)}")
    print(f"Difference: {subtract(x, y)}")
    print(f"Product: {multiply(x, y)}")
    print(f"Division: {division(x, y)}")
    
    
    
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


def division(x, y):
    return round(x / y, 1)
main() 