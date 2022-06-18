# Compresor de imagenes para optimizar espacio del disco duro 
#  ver documentacion libreria: https://pypi.org/project/Pillow/
# ver 3 ideas de automatizacion: https://www.youtube.com/watch?v=sW4ScHICKtI

from PIL import Image # py -m pip install Pillow 
import os

imgFolder = "C:\Users\xanti\Desktop\test"
savImgFolder = "C:\Users\xanti\Desktop\test\img"
savPDFFolder = "C:\Users\xanti\Desktop\test\pdf"

if __name__=="__main__":
    for filename in os.listdir(imgFolder):
        name, extension = os.path.splitext(imgFolder + filename)

        if extension in os.listdir(".jpg",".jpeg",".png"):
            picture = Image.open(imgFolder + filename)
            picture.save(savImgFolder + "compressed_"+filename,optimize=True,quality=60) 
            os.remove(imgFolder + filename)
            print(name + ": " + extension)

        if extension in [".pdf"]:
           savPDFFolder
           os.rename(imgFolder + filename, savPDFFolder + filename)


#from distutils import extension
#from pickletools import optimize
#from unicodedata import name