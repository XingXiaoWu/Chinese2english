就总有憨憨UI，出图给个中文命名，改的我都快气死了😤

因此我用我有限的py知识，写了个这个憨憨小工具

可以直接把文件夹下的中文命名的图片（其实是任意文件）转为英文名，规则是下划线。

不过因为知识有限，图片较多的时候，软件看起来会卡主（其实并没有卡，只是在运行，你不用管它，放在那，过一会就好了）

打包命令

```
sudo pyinstaller --windowed --onefile --clean --noconfirm index.py
```

产物[下载](https://github.com/XingXiaoWu/Chinese2english/releases)

效果图![img](./imgs/img.gif)
