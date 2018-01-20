fileName = input("Enter the file name: ")
wageReport = open(fileName + '.txt', "r")
report = wageReport.read()
print(report)
