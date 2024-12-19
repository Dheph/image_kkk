
import sys
from PIL import Image
import os

def open_kkk(file):
    try:
        with open(file, "r") as f:
            lines = f.read().splitlines()

        dimensions = lines[1].split("x")
        width, height = int(dimensions[0]), int(dimensions[1])

        pixels_hex = lines[2].split(' ')
        pixels = [(int(px[:2], 16), int(px[2:4], 16), int(px[4:], 16)) for px in pixels_hex]

        img = Image.new("RGB", (width, height))
        img.putdata(pixels)
        img.show()

    except Exception as e:
        print(f"Erro ao abrir o arquivo .KKK: {e}")

if __name__ == "__main__":
    kkk_files = [
        os.path.abspath(arg)
        for arg in sys.argv[1:]
        if arg.endswith(".kkk") and os.path.isfile(arg)
    ]

    if not kkk_files:
        print("Erro: Nenhum arquivo .KKK válido foi fornecido.")
    else:
        for file in kkk_files:
            open_kkk(file)

