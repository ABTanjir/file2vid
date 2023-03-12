# CONVERT BINARY STRING TO FILE
from bitstring import BitArray

def run(filePath: str, outputFileName: str):
    f = open(filePath, "r")
    my_str = f.read();
    binary_file = open(outputFileName, 'wb')
    b = BitArray(bin=my_str)
    b.tofile(binary_file)
    binary_file.close()
