# WAP to demonstrate simple exception handling in Python
def ExceptionHandling():
    try:
        a += 10
    except NameError as e:
        print(e)

def main():
    ExceptionHandling()

if __name__ == "__main__":
    main()