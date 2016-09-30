# InternationalizationScript-iOS

# 国际化脚本工具

## 运行环境需求
1. Mac OS X 
2. Python 2.7
3. 安装xlrd1.0 （excel导出到本地化Demo中附带）官方网址：http://pypi.python.org/pypi/xlrd
4. xlrd安装方法 进入xlrd源代码目录 执行 `sudo python setup.py install`
5. 安装xlwt1.1.2 （本地化文件导入到excelDemo中附带）官方网址：https://pypi.python.org/pypi/xlwt
6. xlwt安装方法 进入xlwt源代码目录 执行 `sudo python setup.py install`

## importDemo Excel中数据导入为Localizable.strings 本地化文件

- 将数据excel与执行脚本(importLocalizable.py)放置在一个目录下 Demo目录可以直接使用
- 终端执行命令 `python importLocalizable.py xxx.xls`

## exportDemo 本地化文件导出到Excel中
- 将需要导出的多个Localizable.strings本地化语言文件 重命名，修改执行脚本中的 `paths=["Localizable_en.strings","Localizable_zh-Hans.strings"]`
- 将`Localizable_zh-Hans.strings` `Localizabel_en.strings` 等文件与执行脚本（exportToExcelv2.0.py）放置一个目录下 Demo目录可以直接使用
- 终端执行命令 python exportToExcelv2.0.py

## have fun
