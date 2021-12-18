
from PyQt6 import QtCore, QtGui, QtWidgets
from Imageprocessing import Full


class Ui_Form(QtWidgets.QMainWindow, Full):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 414)
        icon = QtGui.QIcon.fromTheme("python")
        Form.setWindowIcon(icon)
        self.Heading = QtWidgets.QLabel(Form)
        self.Heading.setGeometry(QtCore.QRect(20, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Heading.setFont(font)
        self.Heading.setStyleSheet("")
        self.Heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Heading.setObjectName("Heading")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 80, 231, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Normal = QtWidgets.QRadioButton(self.widget, clicked = lambda : Form.showMinimized())
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Normal.setFont(font)
        self.Normal.setObjectName("Normal")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Normal)
        self.verticalLayout.addWidget(self.Normal, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.Face = QtWidgets.QRadioButton(self.widget, clicked = lambda : Form.showMinimized())
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Face.setFont(font)
        self.Face.setObjectName("Face")
        self.buttonGroup.addButton(self.Face)
        self.verticalLayout.addWidget(self.Face, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)      
        self.TT = QtWidgets.QRadioButton(self.widget, clicked = lambda : Form.showMinimized())
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TT.setFont(font)
        self.TT.setObjectName("TT")
        self.buttonGroup.addButton(self.TT)
        self.verticalLayout.addWidget(self.TT, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.Privacy = QtWidgets.QRadioButton(self.widget, clicked = lambda : Form.showMinimized())
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Privacy.setFont(font)
        self.Privacy.setObjectName("Privacy")
        self.buttonGroup.addButton(self.Privacy)
        self.verticalLayout.addWidget(self.Privacy, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.Normal.clicked.connect(self.on_click)
        self.Face.clicked.connect(self.on_click)
        self.TT.clicked.connect(self.on_click)
        self.Privacy.clicked.connect(self.on_click)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Privacy Screenshot"))
        self.Heading.setText(_translate("Form", "Choose a Mode!"))
        self.Normal.setText(_translate("Form", "Normal"))
        self.Face.setText(_translate("Form", "Taskbar"))
        self.TT.setText(_translate("Form", "Tabs"))
        self.Privacy.setText(_translate("Form", "Privacy (Both)"))

    def on_click(self):
        if self.Normal.isChecked():
            Full.normalClicked()
        elif self.Face.isChecked():
            Full.taskbarClicked()
        elif self.TT.isChecked():
            Full.tabsClicked()
        elif self.Privacy.isChecked():
            Full.privacyClicked()
        






