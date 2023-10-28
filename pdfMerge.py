from pypdf import PdfMerger

fileName = input("File name: ")
fileNumber = int(input("Number of files: "))
outputName = input("Output name: ")

merger = PdfMerger()

i=1
while i < fileNumber:
    merger.append(fileName + str(i) + ".pdf")
    i+=1

merger.write(f"{outputName}.pdf")
merger.close()

print("Files merged successfully")