# WAP to demonstrate multiple exception blocks

def MultipleExceptionHandling():
    try:
        a = 10
        b = eval(input("Enter denominator: "))
        result = a / b
        print(result)
    except ZeroDivisionError as zde:
        print("Zero Division Error: ", zde)
    except Exception as e:
        print("Generic Exception occurred", e)
    else:
        print("Else block executed: No exceptions found")
    finally:
        print("Finally block executed!")
    
def main():
    MultipleExceptionHandling()

if __name__ == "__main__":
    main()
