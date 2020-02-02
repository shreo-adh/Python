from PIL import Image, ImageFilter

img = Image.open(r"C:\Users\USER\Desktop\PYTHON\Pokemon_image\charmander.png")


print(f"\n{img.size}")
hey = img.resize((1000, 1000))
hey.save(r"C:\Users\USER\Desktop\PYTHON\Pokemon_image\Image_Processed\charmanderBig.png")
print(f"\n{hey.size}")
