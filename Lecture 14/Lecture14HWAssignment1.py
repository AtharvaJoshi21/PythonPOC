def from_keys(inputDict, values = None):
    result = dict()
    keys = inputDict.keys()
    if type(values) == list:
        i = 0
        for key in keys:
            if i < len(values):
                result[key] = values[i]
                i += 1
                continue
            result[key] = None
    else:
        result = dict.fromkeys(inputDict, values)
    return result

def main():
    inputDict = eval(input('Please enter a dictionary: '))
    inputValues = eval(input('Please enter values to be added: '))
    print(from_keys(inputDict, inputValues))

if __name__ == '__main__':
    main()