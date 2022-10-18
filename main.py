import os

def print_cwd() -> None:
    print(os.getcwd())

def print_hello() -> None:
    print("Hello world!")

if __name__ == "__main__":
    print_cwd()
    print_hello()
