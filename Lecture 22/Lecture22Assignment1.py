# WAP to demo Popen function of subprocess module

import subprocess

def foo():
    print("Executed...")

def main():
    subprocess.call(['echo', '"to stdout"'], preexec_fn=foo)

if __name__ == "__main__":
    main()