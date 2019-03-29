# WAP to explore "psutil" module. ("psutil" added by Google Inc., similar to subprocess)
#     - import os => os.getpid()
#     - psutil.process(os.getpid()) => returns process handle
#     - print the process handle
import os
import psutil

def main():
    proc = psutil.Process(os.getpid())
    print(proc)

if __name__ == "__main__":
    main()