import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
import os
from translate import Translator

# 用来拖拽
class FileEdit(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)

        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            # for some reason, this doubles up the intro slash
            # filepath = str(urls[0].path())[1:]
            filepath = str(urls[0].path())
            # 删除最后一个
            self.setText(filepath)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # 总体布局
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        # 1.输入框
        self.filePathTextFiled = FileEdit("")
        self.filePathTextFiled.setPlaceholderText("请输入包含图片的文件夹地址，也可以直接拖文件夹到本输入框，文件夹！文件夹！文件夹！")
        self.filePathTextFiled.setDragEnabled(True)
        self.filePathTextFiled.setAcceptDrops(True)
        self.filePathTextFiled.setEnabled(True)
        # self.filePathTextFiled.setAcceptDrops(True)
        # self.filePathTextFiled.setAccessibleDescription(True)
        # self.filePathTextFiled.setAccessibleName(True)


        # self.filePathTextFiled1 = QtWidgets.QTextEdit("")
        # self.filePathTextFiled1.setPlaceholderText("请输入图片文件夹地址，可以先拖到终端再复制路径上来")
        # self.filePathTextFiled1.setAcceptDrops(True)
        # self.layout.addWidget(self.filePathTextFiled1)
        # 支持直接拖拽，带file不要紧
        self.layout.addWidget(self.filePathTextFiled)

        # 2.修改CheckBox
        self.rowLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.rowLayout)
        # self.checkBox1 = self.initcheckbox()
        # self.checkBox1.setText("包含@1x")
        # self.checkBox2 = self.initcheckbox()
        # self.checkBox2.setText("包含@2x")
        # self.checkBox3 = self.initcheckbox()
        # self.checkBox3.setText("包含@3x")
        # self.rowLayout.addWidget(self.checkBox1)
        # self.rowLayout.addWidget(self.checkBox2)
        # self.rowLayout.addWidget(self.checkBox3)

        self.button = QtWidgets.QPushButton("开始转换")
        self.rowLayout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

        # 3.添加结果页
        self.resultLabel = QtWidgets.QLabel("当前状态：待转换")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.resultLabel)

    def magic(self):
        self.resultLabel.setText("当前状态：转换中。。。")
        translator = Translator(from_lang="chinese", to_lang="english")
        # 判断当前路径是否为空
        tmppath = self.filePathTextFiled.text()
        if tmppath != "":
            files = os.listdir(tmppath)
            for file_name in files:
                portion = os.path.splitext(file_name)
                # 中文转英文
                tmp = self.chinese2english(portion, translator)
                # 空格转为下划线_,文件首字母小写，下划线后第一个字母转大写
                new_name_first = self.space2_(tmp)
                new_name = new_name_first + portion[1]
                # 拼接路径
                file_name = tmppath + "/" + file_name
                new_name = tmppath + "/" + new_name
                os.rename(file_name, new_name)
        self.resultLabel.setText("当前状态：转换完成")

    def initcheckbox(self):
        return QtWidgets.QCheckBox()

    # 中译英
    def chinese2english(self, portion, translator):
        # portion = os.path.splitext(file_name)
        new_name_first = translator.translate(portion[0])
        return new_name_first

    # 空格转下划线
    def space2_(self, file_name):
        string_list = file_name.split()
        result = ''
        # 这里可以直接用 str_1.join(str2_list)
        for i in range(len(string_list)):
            tmp = string_list[i]
            tmp = tmp.lower()
            if i == 0:
                result = tmp
            else:
                result = result + "_" + tmp
            # 如果结尾是_@_2x需要替换@2x
        result = result.replace('_@', '@')
        result = result.replace('@_', '@')
        result = result.replace('-', '_')
        # result = result.replace('_@_', '@3x')
        return result


if __name__ == '__main__':
    # os.rename("/Users/wuxing/Downloads/tmp路径@3x(1).png", "/Users/wuxing/Downloads/tmppath_@3x_(1).png")
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())

