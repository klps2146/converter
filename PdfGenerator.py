from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  landscape, A3, A4, A5, B3, B4, B5
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics, ttfonts
import os
# pdfmetrics.registerFont(ttfonts.TTFont("hwfs", "/home/xgj/Desktop/reportlab/hwfs.ttf"))


size_list=(A3, A4, A5, B3, B4, B5) # List (width, height)

def generate_pdf_printing(folder_name, pages_path, page_size=size_list[1]): 
    # pages_amount=1代表有一張譜  / 頁數(一頁最多放置兩面譜)
    # file_path 完整路徑 格式： [ [第一組路徑], [第二組路徑], ...]
    # page_size 頁面長寬資料
    c=canvas.Canvas(f'{folder_name}.pdf', pagesize=(page_size[1], page_size[0]))
    # c.drawString(20, 0, 'Hello,World!') 增加文字
    for i in pages_path:
        place=int(i.split('.')[0].split("/")[-1])+1 # 第幾個圖檔
        # c.drawImage(f"2.jpg" ,page_size[1]/2 , 0, width=page_size[1]/2, height=page_size[0])
        if (place+1)%2!=0:
            c.drawImage(f"{i}" ,0, 0, width=page_size[1]/2, height=page_size[0]) 
            # canvas.drawImage(self, image, x,y, width=None,height=None,mask=None)
        elif (place+1)%2==0:
            c.drawImage(f"{i}" ,page_size[1]/2 , 0, width=page_size[1]/2, height=page_size[0])
            c.showPage() # 換頁
    c.save()



    
# generate_pdf_printing("sbcsadd.pdf", 11)