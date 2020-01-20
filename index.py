import sys
from PySide2 import QtCore, QtWidgets, QtGui
from translate import Translator
from chinese2english import Chinese2English
from fileedit import FileEdit


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
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
        self.rowLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.rowLayout)
        # 修改后缀
        # self.initcheckbox()
        self.initStartButton()

    def initStartButton(self):
        self.button = QtWidgets.QPushButton("开始转换")
        self.rowLayout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    def initTextFiled(self):
        self.filePathTextFiled = FileEdit("")
        self.filePathTextFiled.setPlaceholderText("请输入包含图片的文件夹地址，也可以直接拖文件夹到本输入框，文件夹！文件夹！文件夹！")
        self.filePathTextFiled.setDragEnabled(True)
        self.filePathTextFiled.setAcceptDrops(True)
        self.filePathTextFiled.setEnabled(True)
        # 支持直接拖拽，带file不要紧
        self.layout.addWidget(self.filePathTextFiled)

    def magic(self):
        self.resultLabel.setText("当前状态：转换中。。。")
        translator = Translator(from_lang="chinese", to_lang="english")
        # 判断当前路径是否为空
        tmppath = self.filePathTextFiled.text()
        self.chinese2englishInstance.chinese2english(tmppath)
        self.resultLabel.setText("当前状态：转换完成")

    # def initcheckbox(self):
        # self.changelast = QtWidgets.QCheckBox()
        # self.initcheckbox()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
