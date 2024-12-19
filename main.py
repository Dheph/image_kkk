from PIL import Image

cobaia = Image.open("cobaia.jpg")

pixels = list(cobaia.getdata())

def rgb_to_hex(r,g,b):
    return f"{r:02x}{g:02x}{b:02x}"

for i in range(len(pixels)):
    pixels[i] = rgb_to_hex(*pixels[i])

dimension = 'x'.join(map(str,cobaia.size))

pixel_spacing = ' '.join(map(str,pixels))

content = f"KKK\n{dimension}\n{pixel_spacing}"

with open('cobaia.kkk', 'w') as file:
    file.write(content)


file = open('cobaia.kkk', 'r')

kkk_file = file.read()

kkk_splitted = kkk_file.splitlines()

kkk_dimensions = kkk_splitted[1].split('x')

kkk_pixels = kkk_splitted[2].split(' ')

def hex_to_rgb(hex_pixel):
    return (int(hex_pixel[:2],16), int(hex_pixel[2:4],16), int(hex_pixel[4:],16))

for i in range(len(kkk_pixels)):
    kkk_pixels[i] = hex_to_rgb(kkk_pixels[i])


img = Image.new("RGB", (int(kkk_dimensions[0]), int(kkk_dimensions[1])))
img.putdata(kkk_pixels)
img.show()
