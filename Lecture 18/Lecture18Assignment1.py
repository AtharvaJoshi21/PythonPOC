# WAP to accept a rate file from user and print average of petrol prices for maharashtra ,goa and karnataka.

def PrintAveragePetrolPrices(inputFile):
    line = inputFile.readline()
    mhRate = 0
    goRate = 0
    kaRate = 0
    avgMHRate = 0
    avgGORate = 0
    avgKARate = 0
    while line != "":
        print(line, end = '')
        words = str(line).split(" ")
        mhRate += int(words[2])
        goRate += int(words[3])
        kaRate += int(words[4])
        line = inputFile.readline()

    avgMHRate = mhRate / 12
    avgGORate = goRate / 12
    avgKARate = goRate / 12

    return avgMHRate, avgGORate, avgKARate

def main():
    inputFilePath = input("Please enter rate file name: ")
    fd = open(inputFilePath)
    avgMHRate, avgGORate, avgKARate = PrintAveragePetrolPrices(fd)
    print("")
    print("Average Petrol rates are: ")
    print("Mahrashtra: {}, Goa: {}, Karnataka: {}".format(str(avgMHRate), str(avgGORate), str(avgKARate)))
    fdW = open("avg_petrol_ratext.txt","w")
    fdW.write("Average Petrol rates are: \n")
    fdW.write("Mahrashtra: {}, Goa: {}, Karnataka: {}".format(str(avgMHRate), str(avgGORate), str(avgKARate)))
    fdW.close()

if __name__ == "__main__":
    main()