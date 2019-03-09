# Demo of ConfigParser module

import configparser as CFP

def ParseFile(cfgFileName):
    parser = CFP.ConfigParser()
    parser.read(cfgFileName)
    print(parser.sections())
    print(parser.options('General'))
    print(parser.get('General', 'master'))

def main():
    cfgFileName = input("Please enter file name : ")
    ParseFile(cfgFileName)

if __name__ == "__main__":
    main()