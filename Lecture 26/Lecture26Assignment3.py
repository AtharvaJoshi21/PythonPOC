# WAP to demonstrate finally block execution and nested try except

def FinallyDemonstration():
    try:
        fd = open("Lecture_26.txt", "r")
        try:
            fd.write("Hello")
        finally:
            fd.close()
    except Exception as e:
        print(e.args)

def main():
    FinallyDemonstration()

if __name__ == "__main__":
    main()
