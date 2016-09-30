# -*- coding: utf-8 -*-
import codecs
import xlwt

##########################################################
def readKeysFromFilePath(path):
    listKey = []
    for string in codecs.open(path,'r','utf-8').readlines():
        list = string.split(' = ')
        if len(list) >= 2:
            listKey.append(list[0].lstrip('"').rstrip('"'))
    return listKey
##########################################################
def readValuesFromFilePath(path):
    listValue = []
    for string in codecs.open(path,'r','utf-8').readlines():
        list = string.split(' = ')
        if len(list) >= 2:
            listValue.append(list[1].lstrip('"').rstrip('\n').rstrip(';').rstrip('"'))
    return listValue
##########################################################
if __name__ == '__main__':
    #需要对不同的本地化语言文件重命名 例如 en.lproj/Localizable.strings ---> Localizable_en.strings
    #--spaths =["Localizable_en.strings","Localizable_es.strings","Localizable_id.strings","Localizable_ja.strings","Localizable_pt.strings","Localizable_vi.trings","Localizable_zh-Hans.strings","Localizable_zh-Hant.strings","Localizable_ar.strings"]#
    paths=["Localizable_en.strings","Localizable_zh-Hans.strings"]
    #开工处理
    listValue = []
    wb = xlwt.Workbook()
    ws = wb.add_sheet('test')
    listKey = readKeysFromFilePath(paths[0])
    ws.write(0,0,"Key")
    for x in range(len(listKey)):
        ws.write(x+1,0,listKey[x])
    
    for y in range(len(paths)):
        path = paths[y]
        listValue = readValuesFromFilePath(path)
        ws.write(0,y+1,path)
        for x in range(len(listValue)):
            ws.write(x+1,y+1,listValue[x])

    wb.save("localizableToExcel.xls")


