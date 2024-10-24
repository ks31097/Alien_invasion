from PIL import Image, ImageFilter

before = Image.open("/home/kostiantyn/Alien_invasion/ht/picture/picture.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("/home/kostiantyn/Alien_invasion/ht/picture/out.bmp")