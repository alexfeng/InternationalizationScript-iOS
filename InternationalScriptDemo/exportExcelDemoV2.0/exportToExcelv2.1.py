# -*- coding: utf-8 -*-
import os
import codecs
import xlwt

##########################################################
def readKeysAndValuesFromeFilePath(path):
    if path is None:
        return
    listKey = []
    listValue = []
    for string in codecs.open(path,'r','utf-8').readlines():
        list = string.split(' = ')
        if len(list) >= 2:
            listKey.append(list[0].lstrip('"').rstrip('"'))
            listValue.append(list[1].lstrip('"').rstrip('\n').rstrip(';').rstrip('"'))
    print (listKey)
    print ("+++++++++")
    print (listValue)
    return (listKey,listValue)

##########################################################
def exportToExcel():
    directory = "iOSLocal"
    targetFile = "localizableToExcel.xls"
    if directory is not None:
        index = 0
        if targetFile is not None:
            wb = xlwt.Workbook()
            ws = wb.add_sheet('test',cell_overwrite_ok=True)

            for parent, dirnames, filenames in os.walk(directory):
                for dirname in dirnames:
                    # Key 和 国家简码
                    if index == 0:
                        ws.write(0,0,"Key")
                    # iOS 不同的本地化语言文件xx.proj/Localizable.strings xx 对应国际化的国家简码 eg:english -->en; zh-Hans; zh-Hant; vi; pt; fa;
                    countryCode = dirname.split('.')[0]
                    ws.write(0,index+1,countryCode)

                    #Key 和value
                    path = directory+'/'+dirname+'/Localizable.strings'
                    (keys,values) = readKeysAndValuesFromeFilePath(path)
                    # print(keys)
                    # print('======================')
                    # print(values)

                    for x in range(len(keys)):
                        key = keys[x]
                        value = values[x]
                        if (index == 0):
                            ws.write(x+1, 0, key)
                            ws.write(x+1, 1, value)
                        else:
                            ws.write(x+1, index + 1, value)
                    index += 1

            wb.save(targetFile)

##########################################################
def main():
    exportToExcel()
##########################################################
main()