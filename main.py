from rembg import remove
from PIL import Image
input_path = input("Image Path: ")
output_path = input("Output Path: ")
open_image = input("Open image after when finished? (Y/n): ")
input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
print("Background Removed Succesfully !")
if open_image == "Y":
    Image.open(output_path)
else:
    pass
