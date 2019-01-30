from PIL import Image
data = ""
for i in range( 128**2 ):
    data += chr(255) + chr(0) + chr(0)
im = Image.fromstring("RGB", (128,128), data)
im.save("red.png", "PNG")