# WAP to demonstrate user defined exceptions

class SpeedLimitError(Exception):
    def __init__(self, speed):
        self.__speed = speed
    
    def __str__(self):
        return "Speed is : {}".format(str(self.__speed))

class SpeedAboveLimit(SpeedLimitError):
    def __init__(self, speed):
        SpeedLimitError.__init__(self, speed)

class SpeedBelowLimit(SpeedLimitError):
    def __init__(self, speed):
        SpeedLimitError.__init__(self, speed)

def main():
    try:
        while True:
            try:
                speed = eval(input("Please enter speed: "))
                if speed < 20:
                    x = SpeedBelowLimit(speed)
                    raise x
                elif speed > 80:
                    x = SpeedAboveLimit(speed)
                    raise x
                else:
                    print("Speed is now in valid range")
                    break
            except SpeedBelowLimit as sbl:
                print("Speed below limit")
                print(str(sbl))
            except SpeedAboveLimit as sal:
                print("Speed above limit")
                print(str(sal))
    finally:
        print("Exiting...")

if __name__ == "__main__":
    main()