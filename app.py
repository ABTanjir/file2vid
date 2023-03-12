import os
from lib import file2txt
from lib import txt2img
from lib import img2txt
from lib import txt2file


print("1. convert any file to text")
print("2. convert txt to original file")
print("3. convert any file to image")
print("4. revert image to original file")
opt = int(input("Choose an option: "))
tempTxtFile = './temp.txt'

if(opt == 1):
    filePath = input("Drag the file you want to convert: ").strip("'")
    file2txt.run(filePath)
    
if(opt == 2):
    filePath = input("Drag the binary txt file you want to convert: ").strip("'")
    outputFileName = input("Type output File Name: ")
    txt2file.run(filePath, outputFileName)

if(opt == 3):
    filePath = input("Drag the file you want to convert: ").strip("'")
    outputImgName = input("Type the image name (without extention): ")
    file2txt.run(filePath, tempTxtFile)
    txt2img.run(tempTxtFile, outputImgName)

if(opt == 4):
    filePath = input("Drag the image file you want to revert: ").strip("'")
    outputFileName = input("Type the file name: ")
    img2txt.run(filePath, tempTxtFile)
    txt2file.run(tempTxtFile, outputFileName)

try:
    os.remove(tempTxtFile)
except OSError:
    pass
