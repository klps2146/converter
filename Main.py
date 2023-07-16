import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog)
from Convert import ConvertPIC
import GUI
import json
import getpass

json_file_default_path=f"C:/Users/{getpass.getuser()}/AppData/Roaming"
aim_path=f"{json_file_default_path}/Tab Generator/userdatas/bas.json"
def initialize():
    try:
        with open(aim_path, mode='r') as f:
            datas = json.load(f)
            f.close()
            return datas
    except IsADirectoryError: # 路徑為目錄
        print(IsADirectoryError)
        sys.exit()
    except FileNotFoundError: 
        os.chdir(f"{json_file_default_path}")
        try:
            os.mkdir('Tab Generator')         # 建立一個名為 demo 的資料夾
        except:
            pass
        try:
            os.mkdir('Tab Generator/userdatas')   # 建立一個在 demo 資料夾裡的 hello 資料夾
        except:
            pass
        f = os.open(f"{json_file_default_path}/Tab Generator/userdatas/bas.json", os.O_RDWR|os.O_CREAT) 
        initialize()

    # if os.path.isfile(json_file_default_path):
    #     print("檔案存在。")

def update_json(new_data, json_path=aim_path):
    with open(aim_path, "w") as json_file:
        json.dump(new_data, json_file)
        json_file.close()

if __name__ == '__main__':
    print(os.path.abspath(os.getcwd()))

    origional_datas=initialize()
    print(origional_datas)
    new_json_data=GUI.main(aim_path, origional_datas)
    update_json(new_data=new_json_data)

    sys.exit()
    