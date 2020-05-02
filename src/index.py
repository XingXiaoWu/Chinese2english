import sys
from PySide2 import QtCore, QtWidgets, QtGui
from translate import Translator
from chinese2english import Chinese2English
from fileedit import FileEdit
import os, sys
 
# 获取路径
# def getPath(fileName):
	# path = os.path.join(os.path.dirname(sys.argv[0]), fileName)
	# return path
# Chinese2English = getPath('chinese2english')
# FileEdit = getPath('fileedit')

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.prefixTextFiled = FileEdit("")
        self.filePathTextFiled = FileEdit("")
        self.connectorTextFiled = FileEdit("")
        self.chinese2englishInstance = Chinese2English()
        # 总体布局
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.setUI()

        # 2.修改CheckBox

        # self.checkBox1 = self.initcheckbox()
        # self.checkBox1.setText("包含@1x")
        # self.checkBox2 = self.initcheckbox()
        # self.checkBox2.setText("包含@2x")
        # self.checkBox3 = self.initcheckbox()
        # self.checkBox3.setText("包含@3x")
        # self.rowLayout.addWidget(self.checkBox1)
        # self.rowLayout.addWidget(self.checkBox2)
        # self.rowLayout.addWidget(self.checkBox3)

        # self.button = QtWidgets.QPushButton("开始转换")
        # self.rowLayout.addWidget(self.button)
        # self.button.clicked.connect(self.magic)

        # 3.添加结果页
        self.resultLabel = QtWidgets.QLabel("当前状态：待转换")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.resultLabel)

    #     设置UI
    def setUI(self):
        # 设置输入框
        self.initTextFiled()

        # 新建输入框,写前缀
        self.initPrefixTextFiled()
        # 新建输入框,写连接符
        self.initConnectorTextFiled()
        # 修改后缀
        # self.initcheckbox()
        # 添加横向layout
        self.rowLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.rowLayout)
        self.initStartButton()

    def initStartButton(self):
        self.button = QtWidgets.QPushButton("开始转换")
        self.rowLayout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    def initTextFiled(self):
        self.filePathTextFiled.setPlaceholderText("请输入包含图片的文件夹地址，也可以直接拖文件夹到本输入框，文件夹！文件夹！文件夹！")
        self.filePathTextFiled.setDragEnabled(True)
        self.filePathTextFiled.setAcceptDrops(True)
        self.filePathTextFiled.setEnabled(True)
        # 支持直接拖拽，带file不要紧
        self.layout.addWidget(self.filePathTextFiled)

    def initConnectorTextFiled(self):
        self.connectorTextFiled.setPlaceholderText("连接符，默认为_")
        self.connectorTextFiled.setDragEnabled(True)
        self.connectorTextFiled.setAcceptDrops(True)
        self.connectorTextFiled.setEnabled(True)
        self.layout.addWidget(self.connectorTextFiled)

    def initPrefixTextFiled(self):
        self.prefixTextFiled.setPlaceholderText("前缀，默认为空")
        self.prefixTextFiled.setDragEnabled(True)
        self.prefixTextFiled.setAcceptDrops(True)
        self.prefixTextFiled.setEnabled(True)
        self.layout.addWidget(self.prefixTextFiled)


    # 转换入口
    def magic(self):
        self.resultLabel.setText("当前状态：转换中。。。")
        translator = Translator(from_lang="chinese", to_lang="english")
        # 判断当前路径是否为空
        tmppath = self.filePathTextFiled.text()
        tmpprefix = self.prefixTextFiled.text()
        tmpconnector = self.connectorTextFiled.text()
        if tmpconnector == '':
            tmpconnector = '_'
        self.chinese2englishInstance.chinese2english(tmppath, tmpprefix, tmpconnector)
        self.resultLabel.setText("当前状态：转换完成")

    def initcheckbox(self):
        self.changelast = QtWidgets.QCheckBox()
        self.initcheckbox()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
