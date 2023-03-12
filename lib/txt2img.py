from PIL import Image
import numpy as np
WIDTH_PIXEL = 1080 

def run(inputFilePath :str, outputFilePath :str):
    with open(inputFilePath, 'r') as f:
        binaryString = f.read().strip()

    remaining = WIDTH_PIXEL - int(len(binaryString) % WIDTH_PIXEL);
    if remaining > 0:
        binaryString = binaryString+("0"*remaining)

    binary_array = np.array(list(binaryString), dtype=int).reshape((-1, WIDTH_PIXEL))
    image = Image.fromarray(binary_array.astype(np.uint8) * 255)
    image.save(outputFilePath+'.png')
    image.show();


