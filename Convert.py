from PIL import Image
import os

# convert to jpg

class ConvertPIC:
    def __init__(self):
        pass
    def Webp(img_webp, if_del=True):
        for i in img_webp:
            im=Image.open(i).convert("RGB")
            im.save(f"{i.split('.')[0]}.jpg", "jpeg")
    def Gif(img_gif, if_del=True):
        for i in img_gif:
            im=Image.open(i).convert("RGB")
            im.save(f"{i.split('.')[0]}.jpg", "jpeg") 

    # def Png(img_png, if_del=False):
    #     for i in img_png:
    #         im=Image.open(i).convert("RGB")
    #         im.save(f"{i.split('.')[0]}.jpg", "jpeg")
    #         if if_del:
    #             continue
    #         else:
    #             os.remove(i)
    #             continue
            

 