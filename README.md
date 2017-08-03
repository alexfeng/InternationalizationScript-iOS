# InternationalizationScript-iOS

# 国际化脚本工具

## 运行环境需求
1. Mac OS X 
2. Python 2.7
3. 安装xlrd1.0 （excel导出到本地化Demo中附带）官方网址：http://pypi.python.org/pypi/xlrd
4. xlrd安装方法 进入xlrd源代码目录 执行 `sudo python setup.py install`
5. 安装xlwt1.1.2 （本地化文件导入到excelDemo中附带）官方网址：https://pypi.python.org/pypi/xlwt
6. xlwt安装方法 进入xlwt源代码目录 执行 `sudo python setup.py install`

## importLocalizableDemo 将Excel中数据导出为Localizable.strings 本地化文件

- 将excel中的数据与执行脚本(importLocalizable.py)放置在一个目录下 Demo目录可以直接使用
- 终端执行命令 `python importLocalizable.py localizableFromExcel.xls`

## importLocalizableDemoV2.0 将Excel中数据导出为iOS 需要的xx.proj/Localizable.strings 本地化文件
- 将数据excel与执行脚本(importLocalizable.py)放置在一个目录下 Demo目录可以直接使用
- 终端执行命令 `python importLocalizable.py localizableFromExcel.xls`
- 完成会在脚本目录下生成`iOSLocal`文件夹，下面都是可以直接在iOS项目中使用的本地化文件

## exportExcelDemo 本地化文件导出到Excel中
- 将需要导出的多个Localizable.strings本地化语言文件 重命名，修改执行脚本中的 `paths=["Localizable_en.strings","Localizable_zh-Hans.strings"]`
- 将`Localizable_zh-Hans.strings` `Localizabel_en.strings` 等文件与执行脚本（`exportToExcelv2.0.py`）放置一个目录下 Demo目录可以直接使用
- 终端执行命令 `python exportToExcelv2.0.py`

## exportExcelDemoV2.0 iOS本地化文件导出到Excel中
- 将需要导出的多国语言文件夹放置在`iOSLocal` 文件夹中
- 将`iOSLocal`与执行脚本(`exportToExcelv2.1.py`)放置在一个目录下 exportExcelDemoV2.0目录可以直接使用
- 终端执行命令`python exportToExcelv2.1.py` 
- 导出的excel文件是`localizabelToExcel.xls`
- [ ]V2.0版不需要重命名本地化文件名，更简单方便
  
## have fun

## 历史
2013年在正文集团的下属公司（普罗通信）工作时，碰到多次与产品等进行多语言文档进行修改的工作事项，经过多次的手动处理后，突然某天公司对多语言进行了大量修改，手动处理是一个苦活，静静的思考了下写了个简单的导出脚本，简单的导入脚本，都是需要介入手动操作，已经对原来的苦活减少了很多重复繁重的工作。
2015年底换到全通集团下属习悦信息技术有限公司上班，工作闲暇时间看到一个ZYProSoft群里看到有人在进行多语言处理的工作，吐槽这个手动工作量太大。就将以前写的脚本找出来，简单的修改了下，公布出来。
2017年1月19修改了下脚本，完成最初的构想的脚本，今天是腊月二十三（小年）算是一个完成。
2017年8月3日修改了下说明文档中的错误之处。


