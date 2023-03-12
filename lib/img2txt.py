from PIL import Image

# if pixel is tuple do sum
def sum(pixel):
    if(type(pixel) == int): return pixel
    res = 0
    for i in pixel:
        res += i
    return res

def run(imgFilePath: str, sourceTxtPath = 'temp.txt'):
    image = Image.open(imgFilePath)

    width, height = image.size
    binary_string = ""

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            pixel = sum(pixel)
            
            if pixel < 200:
                binary_string += "0"
            else:
                binary_string += "1"

    # Write the binary string to a file
    with open(sourceTxtPath, "w") as file:
        file.write(binary_string)
