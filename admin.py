from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess
from os import kill
import signal
import sys
from db import DB , StaticData
import psutil
import pyperclip

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 580)
        icon = QtGui.QIcon()
        self.database = DB()
        self.static = StaticData()
        icon.addPixmap(QtGui.QPixmap(str(self.static.getRootFolder())+r"/src/ico/fav-touch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.UploadPath_label = QtWidgets.QLineEdit(Dialog)
        self.UploadPath_label.setEnabled(False)
        self.UploadPath_label.setMinimumSize(QtCore.QSize(0, 30))
        self.UploadPath_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 57  9pt \"Yu Gothic Medium\";")
        self.UploadPath_label.setAlignment(QtCore.Qt.AlignCenter)
        self.UploadPath_label.setObjectName("UploadPath_label")
        self.verticalLayout_3.addWidget(self.UploadPath_label)
        self.DownloadPath_label = QtWidgets.QLineEdit(Dialog)
        self.DownloadPath_label.setEnabled(False)
        self.DownloadPath_label.setMinimumSize(QtCore.QSize(0, 30))
        self.DownloadPath_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 57  9pt \"Yu Gothic Medium\";")
        self.DownloadPath_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DownloadPath_label.setObjectName("DownloadPath_label")
        self.verticalLayout_3.addWidget(self.DownloadPath_label)
        self.max_connection_input = QtWidgets.QLineEdit(Dialog)
        self.max_connection_input.setEnabled(True)
        self.max_connection_input.setMinimumSize(QtCore.QSize(0, 30))
        self.max_connection_input.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 57  9pt \"Yu Gothic Medium\";")
        self.max_connection_input.setText("")
        self.max_connection_input.setAlignment(QtCore.Qt.AlignCenter)
        self.max_connection_input.setObjectName("max_connection_input")
        self.verticalLayout_3.addWidget(self.max_connection_input)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uploadPath_btn = QtWidgets.QPushButton(Dialog)
        self.uploadPath_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.uploadPath_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.uploadPath_btn.setFont(font)
        self.uploadPath_btn.setAutoDefault(False)
        self.uploadPath_btn.setDefault(True)
        self.uploadPath_btn.setObjectName("uploadPath_btn")
        self.verticalLayout_2.addWidget(self.uploadPath_btn)
        self.DownloadPath_btn = QtWidgets.QPushButton(Dialog)
        self.DownloadPath_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.DownloadPath_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DownloadPath_btn.setFont(font)
        self.DownloadPath_btn.setAutoDefault(False)
        self.DownloadPath_btn.setDefault(True)
        self.DownloadPath_btn.setObjectName("DownloadPath_btn")
        self.verticalLayout_2.addWidget(self.DownloadPath_btn)
        self.max_connection_btn = QtWidgets.QPushButton(Dialog)
        self.max_connection_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.max_connection_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.max_connection_btn.setFont(font)
        self.max_connection_btn.setAutoDefault(False)
        self.max_connection_btn.setDefault(True)
        self.max_connection_btn.setObjectName("max_connection_btn")
        self.verticalLayout_2.addWidget(self.max_connection_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.url_lable_link = QtWidgets.QLineEdit(Dialog)
        self.url_lable_link.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.url_lable_link.setFont(font)
        self.url_lable_link.setAlignment(QtCore.Qt.AlignCenter)
        self.url_lable_link.setReadOnly(True)
        self.url_lable_link.setObjectName("url_lable_link")
        self.horizontalLayout_3.addWidget(self.url_lable_link)
        self.copy_url_btn = QtWidgets.QPushButton(Dialog)
        self.copy_url_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.copy_url_btn.setAutoDefault(False)
        self.copy_url_btn.setDefault(False)
        self.copy_url_btn.setFlat(False)
        self.copy_url_btn.setObjectName("copy_url_btn")
        self.horizontalLayout_3.addWidget(self.copy_url_btn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 631, 355))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.command_label = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.command_label.setFont(font)
        self.command_label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Verdana\";")
        self.command_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.command_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.command_label.setReadOnly(True)
        self.command_label.setPlainText("")
        self.command_label.setBackgroundVisible(False)
        self.command_label.setCenterOnScroll(False)
        self.command_label.setObjectName("command_label")
        self.verticalLayout_4.addWidget(self.command_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 10, 0, 1, 4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.serv_start_btn = QtWidgets.QPushButton(Dialog)
        self.serv_start_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serv_start_btn.sizePolicy().hasHeightForWidth())
        self.serv_start_btn.setSizePolicy(sizePolicy)
        self.serv_start_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.serv_start_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.serv_start_btn.setFont(font)
        self.serv_start_btn.setStyleSheet("QPushButton{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.serv_start_btn.setAutoDefault(True)
        self.serv_start_btn.setDefault(True)
        self.serv_start_btn.setFlat(False)
        self.serv_start_btn.setObjectName("serv_start_btn")
        self.verticalLayout_5.addWidget(self.serv_start_btn)
        self.conn_devc_btn = QtWidgets.QPushButton(Dialog)
        self.conn_devc_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.conn_devc_btn.setFont(font)
        self.conn_devc_btn.setAutoDefault(False)
        self.conn_devc_btn.setDefault(False)
        self.conn_devc_btn.setObjectName("conn_devc_btn")
        self.verticalLayout_5.addWidget(self.conn_devc_btn)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.OTP_label = QtWidgets.QLabel(Dialog)
        self.OTP_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.OTP_label.setFont(font)
        self.OTP_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.OTP_label.setAlignment(QtCore.Qt.AlignCenter)
        self.OTP_label.setObjectName("OTP_label")
        self.horizontalLayout_4.addWidget(self.OTP_label)
        self.copy_otp_btn = QtWidgets.QPushButton(Dialog)
        self.copy_otp_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.copy_otp_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.copy_otp_btn.setAutoDefault(False)
        self.copy_otp_btn.setDefault(False)
        self.copy_otp_btn.setObjectName("copy_otp_btn")
        self.horizontalLayout_4.addWidget(self.copy_otp_btn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        
        self.conn_devc_btn.setEnabled(False)
        self.copy_otp_btn.setEnabled(False)
        self.copy_url_btn.setEnabled(False)
        self.max_connection_btn.clicked.connect(self.getMaxConnectionn)
        self.serv_start_btn.clicked.connect(self.run_script)
      
        self.uploadPath_btn.clicked.connect(self.get_uploadPath)
        self.DownloadPath_btn.clicked.connect(self.get_downloadPath)
        self.copy_url_btn.clicked.connect(self.copy_link)
        self.copy_otp_btn.clicked.connect(self.copy_otp)
        self.conn_devc_btn.clicked.connect(self.open_connected_device)
        self.DownloadPath_label.setText(self.database.getDownloadFolderPath())
        self.UploadPath_label.setText(str(self.database.getUploadFolderPath()))
        self.max_connection_input.setText(str(self.database.getMaxConnection()))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Panel ~ LFS(Local file Sharing)"))
        self.UploadPath_label.setPlaceholderText(_translate("Dialog", "Set folder path for uploading files"))
        self.DownloadPath_label.setPlaceholderText(_translate("Dialog", "Set folder path for downloadable files"))
        self.max_connection_input.setPlaceholderText(_translate("Dialog", "Set Max client connection to connect server (eg:4)"))
        self.uploadPath_btn.setText(_translate("Dialog", "Upload Path"))
        self.DownloadPath_btn.setText(_translate("Dialog", "Download Path"))
        self.max_connection_btn.setText(_translate("Dialog", "Max Connection"))
        self.label.setText(_translate("Dialog", "Application URL : "))
        self.url_lable_link.setText(_translate("Dialog", "Application not started yet"))
        self.copy_url_btn.setText(_translate("Dialog", "Copy URL"))
        self.serv_start_btn.setText(_translate("Dialog", "START"))
        self.conn_devc_btn.setText(_translate("Dialog", "Connected Devices"))
        self.label_2.setText(_translate("Dialog", "[ For transferring the file make sure you are connected on same NETWORK / Wi-Fi ]"))
        self.OTP_label.setText(_translate("Dialog", "XXXXXX"))
        self.copy_otp_btn.setText(_translate("Dialog", "Copy OTP"))
        self.PROCESS_STARTED = False

    def open_connected_device(self):
        import os 
        os.system("start "+str(self.url_lable_link.text())+"/getConnection")
    def copy_otp(self):
        if(self.PROCESS_STARTED == True):
                pyperclip.copy(self.OTP_label.text())


    def generate_otp(self):
        if(self.PROCESS_STARTED == False):
            from random import randint
            x=''.join(["{}".format(randint(0, 9)) for num in range(0, 6)])
            self.database.setOTP(x)
            self.OTP_label.setText(x)
        else:
            self.OTP_label.setText("XXXXXX")



    def copy_link(self):
        pyperclip.copy(self.url_lable_link.text())


    def message(self,s):
        self.command_label.appendPlainText(s)


    def run_script(self):
        self.database = DB()
        if(self.PROCESS_STARTED == False):
            self.generate_otp()
            self.command_label.clear()
            self.message("Starting Server......")
            self.database.setHost()
            self.process = QProcess()
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.stateChanged.connect(self.handle_state)
            self.process.finished.connect(self.process_finished) 
            self.process.start("python",["app.py"])
            self.getMaxConnectionn()
        else:
            pid = self.process.processId()
            kill(pid,signal.SIGINT)
            processname = "app.py"
            for proc in psutil.process_iter():
                if proc.name() == processname:
                    proc.kill()
            
        
            
    def get_uploadPath(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QMainWindow(), 'Hey! Select a File')
        self.UploadPath_label.setText(folder_path)
        self.database.setUploadFolderPath(folder_path)

    def get_downloadPath(self):
        folder_paths = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QMainWindow(), 'Hey! Select a File')
        self.DownloadPath_label.setText(folder_paths)
        self.database.setDownloadFolderPath(folder_paths)


    def getMaxConnectionn(self):
        conne = self.max_connection_input.text()
        try:
            conne=int(conne)
            self.database.setMaxConnection(conne)
        except:
            self.database.setMaxConnection(4)

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        try:
            stderr = bytes(data).decode("utf8")
            self.message(stderr)
        except:
            self.message("[----------]")

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        try:
            stdout = bytes(data).decode("utf8")
            self.message(stdout)
        except:
            self.message("[----------]")
        

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        if(state_name=='Running'):
            self.PROCESS_STARTED = True
            self.url_lable_link.setText("http://"+str(self.database.getHOST())+":"+str(self.database.getPORT()))
            self.serv_start_btn.setText("STOP")
            self.max_connection_input.setDisabled(True)
            self.DownloadPath_btn.setDisabled(True)
            self.uploadPath_btn.setDisabled(True)
            self.max_connection_btn.setDisabled(True)
            self.conn_devc_btn.setEnabled(True)
            self.copy_otp_btn.setEnabled(True)
            self.copy_url_btn.setEnabled(True)
        else:
            self.serv_start_btn.setText("START")
            self.url_lable_link.setText("Application not started yet!")
            self.PROCESS_STARTED = False
            self.max_connection_input.setDisabled(False)
            self.DownloadPath_btn.setDisabled(False)
            self.uploadPath_btn.setDisabled(False)
            self.max_connection_btn.setDisabled(False)
        
        self.message(f"Server state: {state_name}")

    def process_finished(self):
        self.message("Server : STOPED")
        self.OTP_label.setText("XXXXXX")
        self.conn_devc_btn.setEnabled(False)
        self.copy_otp_btn.setEnabled(False)
        self.copy_url_btn.setEnabled(False)
        self.process= None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
