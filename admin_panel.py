from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import QProcess
from multimedia import Local_Server,FlushAll,RootFolder
from os import kill
import signal
import sys





class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 350)
        icon = QtGui.QIcon()
        root = RootFolder().getRootFolder()
        icon.addPixmap(QtGui.QPixmap(str(root)+r"/src/ico/fav-touch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
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
        self.url_lable_link = QtWidgets.QLabel(Dialog)
        self.url_lable_link.setEnabled(True)
        self.url_lable_link.setMinimumSize(QtCore.QSize(500, 30))
        self.url_lable_link.setMaximumSize(QtCore.QSize(16777215, 30))
        self.url_lable_link.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Verdana\";")
        self.url_lable_link.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.url_lable_link.setAlignment(QtCore.Qt.AlignCenter)
        self.url_lable_link.setOpenExternalLinks(True)
        self.url_lable_link.setObjectName("url_lable_link")
        self.horizontalLayout_3.addWidget(self.url_lable_link)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 635, 347))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.command_label = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
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
        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 2)
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
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
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
        self.serv_start_btn.setAutoDefault(False)
        self.serv_start_btn.setDefault(True)
        self.serv_start_btn.setFlat(False)
        self.serv_start_btn.setObjectName("serv_start_btn")
        self.gridLayout.addWidget(self.serv_start_btn, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.secure_tnf_chkbx = QtWidgets.QCheckBox(Dialog)
        self.secure_tnf_chkbx.setMinimumSize(QtCore.QSize(30, 20))
        self.secure_tnf_chkbx.setMaximumSize(QtCore.QSize(100, 16777215))
        self.secure_tnf_chkbx.setTristate(False)
        self.secure_tnf_chkbx.setObjectName("secure_tnf_chkbx")
        self.horizontalLayout_4.addWidget(self.secure_tnf_chkbx)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.OTP_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.OTP_label.setFont(font)
        self.OTP_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.OTP_label.setAlignment(QtCore.Qt.AlignCenter)
        self.OTP_label.setObjectName("OTP_label")
        self.gridLayout.addWidget(self.OTP_label, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.retranslateUi(Dialog)
        self.max_connection_btn.clicked.connect(self.getMaxConnectionn)
        self.serv_start_btn.clicked.connect(self.run_script)
        # self.secure_tnf_chkbx.stateChanged.connect(self.setSecure)
        self.uploadPath_btn.clicked.connect(self.get_uploadPath)
        self.DownloadPath_btn.clicked.connect(self.get_downloadPath)
        self.secure_tnf_chkbx.setDisabled(True)


        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Panel ~ LFS(Local file Sharing)"))
        self.label.setText(_translate("Dialog", "Application URL : "))
        self.url_lable_link.setText(_translate("Dialog", "Application not started yet!"))
        self.UploadPath_label.setPlaceholderText(_translate("Dialog", "Set folder path for uploading files"))
        self.DownloadPath_label.setPlaceholderText(_translate("Dialog", "Set folder path for downloadable files"))
        self.max_connection_input.setPlaceholderText(_translate("Dialog", "Set Max client connection (eg:4) Default is : 6 [connection]"))
        self.uploadPath_btn.setText(_translate("Dialog", "Upload Path"))
        self.DownloadPath_btn.setText(_translate("Dialog", "Download Path"))
        self.max_connection_btn.setText(_translate("Dialog", "Max Connection"))
        self.serv_start_btn.setText(_translate("Dialog", "START"))
        self.label_2.setText(_translate("Dialog", "[ For transferring the file make sure you are connected on same NETWORK ]"))
        self.secure_tnf_chkbx.setText(_translate("Dialog", "Secure Transfer"))
        self.OTP_label.setText(_translate("Dialog", "XXXXXX"))
        self.PROCESS_STARTED = False
        




    def message(self,s):
        self.command_label.appendPlainText(s)
    
    def run_script(self):
        if(self.PROCESS_STARTED == False):
            self.command_label.clear()
            self.message("Starting Server......")
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
            
        
            
    def get_uploadPath(self):
        from FNF import FolderPaths
        f = FolderPaths()
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QMainWindow(), 'Hey! Select a File')
        self.UploadPath_label.setText(folder_path)
        f.setUploadFolderPath(folder_path)


    def get_downloadPath(self):
        from FNF import FolderPaths
        f = FolderPaths()
        folder_paths = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QMainWindow(), 'Hey! Select a File')
        self.DownloadPath_label.setText(folder_paths)
        f.setDownloadFolderPath(folder_paths)


    def getMaxConnectionn(self):
        from FNF import FolderPaths
        f=FolderPaths()
        conn = self.max_connection_input.text()
        try:
            conn=int(conn)
            f.setMaxConnection(conn)
        except:
            f.setMaxConnection('4') 

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
        self.server_details = Local_Server()
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        if(state_name=='Running'):
            self.PROCESS_STARTED = True
            self.url_lable_link.setText("http://"+str(self.server_details.HOST)+":"+str(self.server_details.PORT))
            self.serv_start_btn.setText("STOP")
            
            self.max_connection_input.setDisabled(True)
            self.DownloadPath_btn.setDisabled(True)
            self.uploadPath_btn.setDisabled(True)
            self.max_connection_btn.setDisabled(True)
            # metadata.ClearMetaData()
        
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
        flush = FlushAll()
        flush.ClearMetaData()
        self.message("Server : STOPED")
        self.process= None


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

