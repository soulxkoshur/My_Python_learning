from PIL import Image, ImageOps
import sys
import os


def main():
    inputfile = sys.argv[1]
    outputfile  = sys.argv[2]
    extenstions = ['.png', '.jpeg', '.jpg']
    if os.path.splitext(inputfile)[1].lower() not in extenstions :
        sys.exit(" Invalid input")
    elif os.path.splitext(outputfile)[1].lower() != os.path.splitext(inputfile)[1].lower():
        sys.exit("Input and output have different extensions")
    elif os.path.splitext(outputfile)[1].lower() not in extenstions:
        sys.exit("Invalid output")
    else:
        main_logic(sys.argv[1], sys.argv[2] )  


def main_logic( x, y ):
    try:
        image = x
        output_img = y
        if len(sys.argv)<3:
            sys.exit("too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        else:
            image_process(image, output_img)
    except FileNotFoundError:
        sys.exit("file not found!") 


def image_process(image, output):
        img1 = Image.open(image)
        img2 = Image.open('shirt.png')
        size = img2.size
        inputfit = ImageOps.fit(img1, size)
        inputfit.paste(img2, (0, 0), img2)
        inputfit.save(output)
        
main()