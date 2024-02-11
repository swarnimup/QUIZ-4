from folder1 import function1 as func1
from folder2 import function2 as func2
from folder3 import function3 as func3

def main():
    result1 = func1()
    result2 = func2()
    result3 = func3()

    print(f"Result from function1: {result1}")
    print(f"Result from function2: {result2}")
    print(f"Result from function3: {result3}")

if __name__ == "__main__":
    main()
