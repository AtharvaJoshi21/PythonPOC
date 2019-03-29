# WAP to accept a command to be executed as a cmd line arg. Execute the command provided and print output of the same.
import optparse
import subprocess

def ExecCmd(inputCommand):
    execCmdOutput = subprocess.check_output(inputCommand, shell = True)
    return execCmdOutput

def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", help = "Input Command to be executed", dest = "inputCommand")
    (options, args) = parser.parse_args()
    execCommandOutput = ExecCmd(options.inputCommand)
    print("**** Output of the command execution is : ****")
    print(execCommandOutput)

if __name__ == "__main__":
    main()