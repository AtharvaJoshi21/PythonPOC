# WAP which runs periodically and displays the status of currently running processes.
import subprocess
import time

def ProcessStatScheduler(inputTimeInterval):
    breakFlag = True
    while breakFlag:
        outputStats = subprocess.check_output(['ps'])
        print("Process stats are: ")
        print(outputStats)
        print("")
        msgContinue = input('Do you want to continue? [y/n]: ')
        if msgContinue == 'n' or msgContinue == 'N':
            break
        time.sleep(inputTimeInterval)

def main():
    inputTimeInterval = eval(input("Please enter interval: "))
    ProcessStatScheduler(inputTimeInterval)

if __name__ == "__main__":
    main()
