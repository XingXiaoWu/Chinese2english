import os
from translate import Translator


class Chinese2English:
    def __init__(self):
        self.translator = Translator(from_lang="chinese", to_lang="english")

    def translate(self, portion):
        new_name_first = self.translator.translate(portion[0])
        return new_name_first

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
        result = result.replace('_@', '@')
        result = result.replace('@_', '@')
        result = result.replace('-', '_')
        return result

    def chinese2english(self, path):
        # 判断路径是否为空
        if path == "":
            return False
        else:
            files = os.listdir(path)
            for file_name in files:
                portion = os.path.splitext(file_name)
                # 中文转英文
                tmpName = self.translate(portion)
                # 空格转为下划线_, 文件首字母小写，下划线后第一个字母转大写
                new_name_first = self.space2_(tmpName)
                new_name = new_name_first + portion[1]
                # 拼接路径
                file_name = path + "/" + file_name
                new_name = path + "/" + new_name
                os.rename(file_name, new_name)
        return True
