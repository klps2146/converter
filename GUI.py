from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from Convert import ConvertPIC
import PdfGenerator
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog)

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.document_type=[] # 檔案格式 格式：[第一組資料的格式, 第二組資料的格式, ...]("normal" / "gif" / "webp") 
        self.file_list_place=0 
        self.files_path=[] # 完整路徑 格式： [ [第一組路徑], [第二組路徑], ...]
        self.acoustic_fingerstyle_path=r"C:\Users\klps2\OneDrive\Guitar Tab Active\Acoustic Fingerstyle"
        self.solo_fingerstyle_path=r"C:\Users\klps2\OneDrive\Guitar Tab Active\Solo FIngerstyle"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 820)
        MainWindow.setMinimumSize(QtCore.QSize(580, 820))
        MainWindow.setMaximumSize(QtCore.QSize(812, 1100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(3840, 1920))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        #### 按鈕 ####
        # 導入按鈕
        self.import_file = QtWidgets.QPushButton(self.centralwidget)
        self.import_file.setMinimumSize(QtCore.QSize(220, 40))
        self.import_file.setMaximumSize(QtCore.QSize(230, 50))
        self.import_file.clicked.connect(self.import_file_button)

        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.import_file.setFont(font)
        self.import_file.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.import_file.setStyleSheet("background-color: rgb(213, 248, 255);\n"
"")
        self.import_file.setObjectName("import_file")
        self.horizontalLayout.addWidget(self.import_file)


        # Layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(8)


        # Lebal
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        # 預設路徑 輸入框 
        self.default_path = QtWidgets.QLineEdit(self.centralwidget)
        self.default_path.setMinimumSize(QtCore.QSize(0, 30))
        self.default_path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.default_path.setObjectName("default_path")

        # Layout
        self.verticalLayout_2.addWidget(self.default_path)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 紀錄選擇路徑 list
        self.path_record = QtWidgets.QListWidget(self.centralwidget)
        self.path_record.setMaximumSize(QtCore.QSize(5000, 6000))
        self.path_record.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.path_record.setObjectName("path_record")
        self.verticalLayout.addWidget(self.path_record)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)


        # 進度條
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0) # 設定進度
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")


        #### 按鈕 ####
        # 開始轉換按鈕
        self.convert_save = QtWidgets.QPushButton(self.centralwidget)
        self.convert_save.setMinimumSize(QtCore.QSize(335, 60))
        self.convert_save.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        self.convert_save.setFont(font)
        self.convert_save.setStyleSheet("background-color: rgb(224, 255, 219);")
        self.convert_save.setObjectName("convert_save")
        self.horizontalLayout_3.addWidget(self.convert_save)

        self.convert_save.clicked.connect(self.convert_and_save)

        # 重新選擇按鈕
        self.rechose = QtWidgets.QPushButton(self.centralwidget)
        self.rechose.setMinimumSize(QtCore.QSize(0, 60))
        self.rechose.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        self.rechose.setFont(font)
        self.rechose.setStyleSheet("background-color: rgb(255, 226, 226);")
        self.rechose.setObjectName("rechose")
        self.horizontalLayout_3.addWidget(self.rechose)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 5, -1, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.rechose.clicked.connect(self.cancel_selected)


        #### Check Box ####
        # 增加瀏覽用 PDF
        self.create_browse_pdf = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.create_browse_pdf.setFont(font)
        self.create_browse_pdf.setObjectName("create_browse_pdf")
        self.gridLayout.addWidget(self.create_browse_pdf, 1, 1, 1, 1)

        self.create_browse_pdf.toggle()

        # 轉換為 JPG
        self.convert_jpg_check = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.convert_jpg_check.setFont(font)
        self.convert_jpg_check.setObjectName("convert_jpg_check")
        self.gridLayout.addWidget(self.convert_jpg_check, 0, 0, 1, 1)

        self.convert_jpg_check.toggle()

        # 保留 WEBP
        self.dont_delet_webp = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dont_delet_webp.setFont(font)
        self.dont_delet_webp.setObjectName("dont_delet_webp")
        self.gridLayout.addWidget(self.dont_delet_webp, 0, 1, 1, 1)

        # self.dont_delet_webp.toggle()

        ## 存到 SOLO
        self.save_solo_folder = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        self.save_solo_folder.setFont(font)
        self.save_solo_folder.setObjectName("save_solo_folder")
        self.gridLayout.addWidget(self.save_solo_folder, 3, 1, 1, 1)

        # 增加列印用 PDF
        self.create_print_pdf = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.create_print_pdf.setFont(font)
        self.create_print_pdf.setObjectName("create_print_pdf")
        self.gridLayout.addWidget(self.create_print_pdf, 1, 0, 1, 1)

        self.create_print_pdf.toggle()

        ## 存到 Acoustic
        self.save_acoustic_folder = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        self.save_acoustic_folder.setFont(font)
        self.save_acoustic_folder.setObjectName("save_acoustic_folder")
        self.gridLayout.addWidget(self.save_acoustic_folder, 3, 0, 1, 1)



        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 18))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuhh = QtWidgets.QMenu(self.menubar)
        self.menuhh.setGeometry(QtCore.QRect(245, 113, 127, 76))
        self.menuhh.setObjectName("menuhh")
        self.menulanguage = QtWidgets.QMenu(self.menuhh)
        self.menulanguage.setObjectName("menulanguage")
        self.menuFolder_Path = QtWidgets.QMenu(self.menuhh)
        self.menuFolder_Path.setObjectName("menuFolder_Path")
        self.menuSolo_Fingerstyle = QtWidgets.QMenu(self.menuFolder_Path)
        self.menuSolo_Fingerstyle.setObjectName("menuSolo_Fingerstyle")
        self.menuAcoustic_Fingerstyle = QtWidgets.QMenu(self.menuFolder_Path)
        self.menuAcoustic_Fingerstyle.setObjectName("menuAcoustic_Fingerstyle")
        self.menuDefault_Path = QtWidgets.QMenu(self.menuFolder_Path)
        self.menuDefault_Path.setObjectName("menuDefault_Path")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuBackground_Color = QtWidgets.QMenu(self.menu)
        self.menuBackground_Color.setObjectName("menuBackground_Color")
        self.menuPath_Color = QtWidgets.QMenu(self.menu)
        self.menuPath_Color.setObjectName("menuPath_Color")
        self.menuWindow_Position = QtWidgets.QMenu(self.menu)
        self.menuWindow_Position.setObjectName("menuWindow_Position")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionbfcb = QtWidgets.QAction(MainWindow)
        self.actionbfcb.setObjectName("actionbfcb")
        self.actionTraditional_Chinese = QtWidgets.QAction(MainWindow)
        self.actionTraditional_Chinese.setObjectName("actionTraditional_Chinese")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionDefault_2 = QtWidgets.QAction(MainWindow)
        self.actionDefault_2.setObjectName("actionDefault_2")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionHide = QtWidgets.QAction(MainWindow)
        self.actionHide.setObjectName("actionHide")
        self.actionBrose = QtWidgets.QAction(MainWindow)
        self.actionBrose.setObjectName("actionBrose")
        self.actionBrowse = QtWidgets.QAction(MainWindow)
        self.actionBrowse.setObjectName("actionBrowse")
        self.actionBrowse_2 = QtWidgets.QAction(MainWindow)
        self.actionBrowse_2.setObjectName("actionBrowse_2")
        self.actionDefault_3 = QtWidgets.QAction(MainWindow)
        self.actionDefault_3.setObjectName("actionDefault_3")
        self.actionFixed_On_Top = QtWidgets.QAction(MainWindow)
        self.actionFixed_On_Top.setObjectName("actionFixed_On_Top")
        self.actionBottom = QtWidgets.QAction(MainWindow)
        self.actionBottom.setObjectName("actionBottom")
        self.menulanguage.addAction(self.actionTraditional_Chinese)
        self.menuSolo_Fingerstyle.addAction(self.actionBrose)
        self.menuAcoustic_Fingerstyle.addAction(self.actionBrowse)
        self.menuDefault_Path.addAction(self.actionBrowse_2)
        self.menuFolder_Path.addAction(self.menuDefault_Path.menuAction())
        self.menuFolder_Path.addSeparator()
        self.menuFolder_Path.addAction(self.menuAcoustic_Fingerstyle.menuAction())
        self.menuFolder_Path.addAction(self.menuSolo_Fingerstyle.menuAction())
        self.menuhh.addAction(self.menulanguage.menuAction())
        self.menuhh.addAction(self.menuFolder_Path.menuAction())
        self.menuBackground_Color.addAction(self.actionDark)
        self.menuBackground_Color.addAction(self.actionLight)
        self.menuBackground_Color.addAction(self.actionDefault)
        self.menuPath_Color.addAction(self.actionDefault_2)
        self.menuPath_Color.addAction(self.actionGreen)
        self.menuPath_Color.addAction(self.actionRed)
        self.menuPath_Color.addSeparator()
        self.menuPath_Color.addAction(self.actionHide)
        self.menuWindow_Position.addAction(self.actionDefault_3)
        self.menuWindow_Position.addSeparator()
        self.menuWindow_Position.addAction(self.actionFixed_On_Top)
        self.menu.addAction(self.menuBackground_Color.menuAction())
        self.menu.addAction(self.menuPath_Color.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.menuWindow_Position.menuAction())
        self.menubar.addAction(self.menuhh.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.default_path.setText(_translate("MainWindow", "C:\\Users\\klps2\\OneDrive\\Guitar Tab Active"))
        self.import_file.setText(_translate("MainWindow", "導入"))
        self.label.setText(_translate("MainWindow", "預設路徑"))
        self.convert_save.setText(_translate("MainWindow", "轉換並儲存"))
        self.rechose.setText(_translate("MainWindow", "重新選取"))
        self.create_browse_pdf.setText(_translate("MainWindow", "新增瀏覽用pdf"))
        self.convert_jpg_check.setText(_translate("MainWindow", "轉換為jpg"))
        self.dont_delet_webp.setText(_translate("MainWindow", "保留wepb"))
        self.save_solo_folder.setText(_translate("MainWindow", "存至 Solo Fingerstyle 資料夾"))
        self.create_print_pdf.setText(_translate("MainWindow", "新增影印用pdf"))
        self.save_acoustic_folder.setText(_translate("MainWindow", "存至 Acoustic Fingerstyle 資料夾"))
        self.menuhh.setTitle(_translate("MainWindow", "設定"))
        self.menulanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuFolder_Path.setTitle(_translate("MainWindow", "Folder Path"))
        self.menuSolo_Fingerstyle.setTitle(_translate("MainWindow", "Solo Fingerstyle"))
        self.menuAcoustic_Fingerstyle.setTitle(_translate("MainWindow", "Acoustic Fingerstyle"))
        self.menuDefault_Path.setTitle(_translate("MainWindow", "Default Path"))
        self.menu.setTitle(_translate("MainWindow", "檢視"))
        self.menuBackground_Color.setTitle(_translate("MainWindow", "Background Color"))
        self.menuPath_Color.setTitle(_translate("MainWindow", "Path Color"))
        self.menuWindow_Position.setTitle(_translate("MainWindow", "Window Position"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionbfcb.setText(_translate("MainWindow", "bfcb"))
        self.actionTraditional_Chinese.setText(_translate("MainWindow", "Traditional Chinese"))
        self.actionDark.setText(_translate("MainWindow", "Default"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionDefault.setText(_translate("MainWindow", "Dark"))
        self.actionDefault_2.setText(_translate("MainWindow", "Default"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionHide.setText(_translate("MainWindow", "Hide"))
        self.actionBrose.setText(_translate("MainWindow", "Browse"))
        self.actionBrowse.setText(_translate("MainWindow", "Browse"))
        self.actionBrowse_2.setText(_translate("MainWindow", "Browse"))
        self.actionDefault_3.setText(_translate("MainWindow", "Default"))
        self.actionFixed_On_Top.setText(_translate("MainWindow", "Fixed On Top"))
        self.actionBottom.setText(_translate("MainWindow", "Bottom"))



    #### reaction ####\
    def group_check(self):
        pass


    def import_file_button(self):
        self.process_bar_setting(0)
        filename = QFileDialog.getOpenFileNames(self, '開啟檔案', filter='webp (*.webp);;gif(*.gif);;normal (*.jpg *.jpeg *.png)', directory=str(self.default_path.text()))
        if filename[1]=="webp (*.webp)":
            self.files_path.append(filename[0])
            self.document_type.append("webp")
            self.file_path_list_setting()
        elif filename[1]=="gif(*.gif)":
            self.files_path.append(filename[0])
            self.document_type.append("gif")
            self.file_path_list_setting()
        elif filename[1]=="normal (*.jpg *.jpeg *.png)":
            self.files_path.append(filename[0])
            self.document_type.append("normal")
            self.file_path_list_setting()

    def process_bar_setting(self, values): 
        self.progressBar.setProperty("value", values)

    def file_path_list_setting(self):  # 加入至顯示列表中
        for i in self.files_path[self.file_list_place]:
            print(i)
            ips=".../"+i.split("/")[-2]+"/"+i.split("/")[-1]
            self.path_record.addItem(str(ips)) # 加入至顯示列表中
        else:    
            self.file_list_place+=1
            print(self.files_path)
            print(self.file_list_place)

    def file_path_list_add(self, datas):
        if type(datas)==str or int or float:
            self.path_record.addItem(str(datas))
        # elif type(datas)==list:
            # for f in datas:
                # self.path_record.addItem(str(f))
        # elif type(datas)==dict:
        #     for h in datas:
        #         self.path_record.addItem(str(f"{h}: {datas[h]}"))

    def file_list_results(self, mode=""):
        pass

    def cancel_selected(self):
        self.process_bar_setting(0)
        for i in self.files_path:        
            for j in i:
                self.path_record.removeItemWidget(self.path_record.takeItem(0))
                self.path_record.removeItemWidget(self.path_record.takeItem(0))
        else:
            self.files_path=[]
            self.file_list_place=0

    def cancel_selected_after(self):
        for i in self.files_path:        
            for j in i:
                self.path_record.removeItemWidget(self.path_record.takeItem(0))
        else:
            self.files_path=[]
            self.file_list_place=0

    def sort_path(self):
        full_path_place=-1
        for i in self.files_path:
            full_path_place+=1
            after_sort={}
            for j in i:
                after_sort[(f"{j.split('.')[0].split('/')[-1]}")]=j
            sorted_list=sorted(after_sort)
            output_path=[]
            for i in sorted_list:
                output_path.append(after_sort[i])
            self.files_path[full_path_place]=output_path
            print(self.files_path)

    def convert_and_save(self): # 主執行序列 (開始轉換按鈕觸發)
        if self.files_path!=[]:
            self.sort_path()
            self.process_bar_setting(5)
            self.process_bar_setting(40)
            self.convert_moudle(self.check_box_collecting())
            self.process_bar_setting(80)
            self.cancel_selected_after()
            self.process_bar_setting(100)
            self.file_path_list_add("完成：")
            # self.file_path_list_add({"jpg":"1.jpg"})
        else:
            self.file_path_list_add("請先選擇檔案")

    def convert_moudle(self, datas=[0,0,0,False,0,0]): # 主要轉換及製作動作 (所有檔案做同樣動作 僅路徑不同)
# [增加瀏覽用 PDF,增加列印用 PDF, 轉換為 JPG, 保留   WEBP, 存到 SOLO, 存到 Acoustic, state]// 0 為未勾選
# [      0      ,       1     ,      2   ,      3     ,      4   ,       5     ,  (6) ]
        if datas[2]==1: # 轉換成JPG
            folder_place=-1
            for one_path in self.files_path:
                folder_place+=1
                if self.document_type[folder_place]=="webp":
                    ConvertPIC.Webp(img_webp=one_path, if_del=datas[3]) # 轉換成WEBP
                    if datas[1]==1: # Generate PDF for printing
                        name_f=one_path[0].split("/")[-2] # 僅有圖片資料夾的名稱 (圖片皆需為.jpg)
                        PdfGenerator.generate_pdf_printing(folder_name=name_f, pages_path=one_path)
                    
                    if datas[0]==1:
                        pass

                elif self.document_type[folder_place]=="gif":
                    ConvertPIC.Gif(img_webp=one_path, if_del=datas[3]) # 轉換成GIF
                    if datas[1]==1: # Generate PDF 
                        name_f=one_path[0].split("/")[-2] # 僅有圖片資料夾的名稱 (圖片皆需為.jpg)
                        PdfGenerator.generate_pdf_printing(folder_name=name_f, pages_path=one_path)

                elif self.document_type[folder_place]=="normal":
                    if datas[1]==1: # Generate PDF 
                        name_f=one_path[0].split("/")[-2] # 僅有圖片資料夾的名稱 (圖片皆需為.jpg)
                        PdfGenerator.generate_pdf_printing(folder_name=name_f, pages_path=one_path)
                    
                if datas[3]==False: # 不保留Webp
                    if self.document_type[folder_place]=="webp":
                        for delet_path in one_path:
                            os.remove(delet_path)

                elif datas[3]==True:
                    if datas[4]==0:

                        if datas[5]==0:
                            pass
                        else:
                            pass
                    else:
                        pass
            else:
                folder_place=-1

        elif datas[2]==0: # 不轉換jpg ==> 轉換jpg  > 產生PDG > 刪除JPG
            folder_place=-1
            for one_path in self.files_path:
                folder_place+=1
                if self.document_type[folder_place]=="webp":
                    ConvertPIC.Webp(img_webp=one_path, if_del=datas[3]) # 轉換成WEBP
                    if datas[1]==1: # Generate PDF for printing
                        name_f=one_path[0].split("/")[-2] # 僅有圖片資料夾的名稱 (圖片皆需為.jpg)
                        PdfGenerator.generate_pdf_printing(folder_name=name_f, pages_path=one_path)
                    
                    if datas[0]==1:
                        pass

                elif self.document_type[folder_place]=="gif":
                    ConvertPIC.Gif(img_webp=one_path, if_del=datas[3]) # 轉換成GIF
                    if datas[1]==1: # Generate PDF 
                        name_f=one_path[0].split("/")[-2] # 僅有圖片資料夾的名稱 (圖片皆需為.jpg)
                        PdfGenerator.generate_pdf_printing(folder_name=name_f, pages_path=one_path)

                elif self.document_type[folder_place]=="normal":
                    if datas[1]==1: # Generate PDF 
                        name_f=one_path[0].split("/")[-2] # 僅有圖片資料夾的名稱 (圖片皆需為.jpg)
                        PdfGenerator.generate_pdf_printing(folder_name=name_f, pages_path=one_path)
                
                for delet_jpg in one_path:
                    os.remove(str(delet_jpg.split(".")[-2]))

                if datas[3]==False: # 不保留Webp
                    if self.document_type[folder_place]=="webp":
                        for delet_path in one_path:
                            os.remove(delet_path)

                elif datas[3]==True:
                    if datas[4]==0:

                        if datas[5]==0:
                            pass
                        else:
                            pass
                    else:
                        pass
            else:
                folder_place=-1



    def check_box_collecting(self):
        # datas content [增加瀏覽用 PDF,增加列印用 PDF, 轉換為 JPG, 不刪除 WEBP, 存到 SOLO, 存到 Acoustic, state]
        datas=[0, 0, 0, 0, 0, 0]
        if self.create_browse_pdf.isChecked():
            datas[0]=1
        else:
            datas[0]=0
        if self.create_print_pdf.isChecked():
            datas[1]=1
        else:
            datas[1]=0
        if self.convert_jpg_check.isChecked():
            datas[2]=1
        else:
            datas[2]=0
        if self.dont_delet_webp.isChecked():
            datas[3]=True
        else:
            datas[3]=False
        if self.save_solo_folder.isChecked():
            datas[4]=1
        else:
            datas[4]=0
        if self.save_acoustic_folder.isChecked():
            datas[5]=1
        else:
            datas[5]=0

        return datas


    def clear_selected(self):
        self.files_path=[]
        self.document_type=""


#if __name__ == "__main__":
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
