# CONVERT FILE TO BINARY STRING
def saveStr(filePath, data):
    with open(filePath, "w") as text_file:
        text_file.write(data)
    
def run(filePath, outputPath = 'binary.txt'):
    with open(filePath, 'rb') as file:
        byte = file.read(1)
        binary_string = ""
        while byte:
            binary_string += bin(ord(byte))[2:].zfill(8)
            byte = file.read(1)
        saveStr(outputPath, binary_string)
        print("File saved as "+outputPath);