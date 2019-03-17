# WAP to read columns from an excel sheet and create a vcf out of columns.
import openpyxl

def CreateVCF(row):
    fileName = str("{}.vcf".format(row[0].value))
    destContactFile = open(fileName, "w")
    fileString = 'BEGIN:VCARD\n'
    fileString += 'VERSION:3.0\n'
    fileString += str('FN:{}\n'.format(str(row[0].value)))
    fileString += str('EMAIL:{}\n'.format(str(row[1].value)))
    fileString += str('TEL;WORK;VOICE:{}\n'.format(str(row[2].value)))
    fileString += str('ORG:{}\n'.format(str(row[3].value)))
    fileString += 'END:VCARD\n'
    destContactFile.write(fileString)
    destContactFile.close()

def ReadExcel(inputFilePath):
    workBook = openpyxl.load_workbook(inputFilePath)
    sheet_ranges = workBook[workBook.get_sheet_names()[0]]
    for row in sheet_ranges.iter_rows():
        CreateVCF(row)

def main():
    srcContactsFilePath = input("Please select the source file: ")
    ReadExcel(srcContactsFilePath)
    print("VCF Files created successfully!")
    # srcContactsFileFD = open(srcContactsFilePath)

if __name__ == "__main__":
    main()