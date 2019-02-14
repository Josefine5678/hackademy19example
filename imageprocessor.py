from PIL import Image
import code
import os

def rotate_box(an_image):
    box = (100,100,200,200)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image 


def to_grayscale(an_image):
    garyscale_im = an_image.convert('LA')
    return garyscale_im 



pic_list = code.get_filenames("C:\\Users\\Josefine\\Desktop\\pictures")
num = 0
for pic_name in pic_list:
    im = Image.open(pic_name)
    im = to_grayscale(im)

    new_filename = "pic_gray_" + str(num) + ".jpg"
    num = num + 1
    newfullpath = os.path.join("C:\\Users\\Josefine\\Desktop\\pictures",new_filename)
    
    im.save(newfullpath)







