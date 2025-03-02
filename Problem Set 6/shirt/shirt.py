import sys
from PIL import Image, ImageOps


def main():
    validate()
    try:
        img = Image.open("shirt.png")
        before = Image.open(sys.argv[1])
        before = ImageOps.fit(before, img.size)
        before.paste(img, box=(0, 0), mask=img)
        before.save(sys.argv[2], format=None)
    except FileNotFoundError:
        sys.exit("Could not find the image file")


def validate():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        extension = [".jpg", ".jpeg", ".png"]
        before, after = sys.argv[1], sys.argv[2]
        if before[-4:].lower() != after[-4:].lower() and before[-4:] in extension:
            sys.exit("Input and output have different extensions")
        elif before[-4:].lower() not in extension:
            sys.exit("Invalid input")
        elif after[-4:].lower() not in extension:
            sys.exit("Invalid output")


main()
