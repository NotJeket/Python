from PIL import Image
import os

#place the path to the folder here \/
source_folder = 'C:\\Users\\RoyalPC1\\Desktop\\test\\white_am\\'
#palce the path to the destiantiopn folder here \/
destination_folder = 'C:\\Users\\RoyalPC1\\Desktop\\test\\white_am_rez\\'
directory = os.listdir(source_folder)

for item in directory:
    img = Image.open(source_folder + item)
    imgResize = img.resize((256, 256))
    imgResize.save(destination_folder + item[:-4] + '.png', quality=100)

for item in directory:
    img = Image.open(source_folder + item)
    imgResize = img.resize((256, 256))
    imgResize.save(destination_folder + item[:-4] + '_256.png', quality=100)

for item in directory:
    img = Image.open(source_folder + item)
    imgResize = img.resize((128, 128))
    imgResize.save(destination_folder + item[:-4] + '_128.png', quality=100)

for item in directory:
    img = Image.open(source_folder + item)
    imgResize = img.resize((64, 64))
    imgResize.save(destination_folder + item[:-4] + '_64.png', quality=100)


