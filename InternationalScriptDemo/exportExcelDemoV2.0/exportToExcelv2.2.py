# -*- coding: utf-8 -*-
# import OptionParser
import os
import codecs
import xlwt

##########################################################
def addParser():
    # parser = OptionParser()
    parser.add_option("-f", "--filePath",
                      help="original.xls File Path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFloderPath",
                      help="Target Floder Path.",
                      metavar="targetFloderPath")
    
    parser.add_option("-i", "--iOSAdditional",
                      help="iOS additional info.",
                      metavar = "iOSAdditional")

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
def exportToExcel(options):
    directory = options.directory #"iOSLocal"
    targetFile = options.targetFile #"localizableToExcel.xls"
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
                    # xx.proj 取xx 表示本地化国家简码
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
        
    #iOS 不同的本地化语言文件xx.proj/Localizable.strings xx 对应国际化的国家简码 eg:english -->en; zh-Hans 
    #需要对不同的本地化语言文件重命名 例如 en.lproj/Localizable.strings ---> Localizable_en.strings
    #--spaths =["Localizable_en.strings","Localizable_es.strings","Localizable_id.strings","Localizable_ja.strings","Localizable_pt.strings","Localizable_vi.trings","Localizable_zh-Hans.strings","Localizable_zh-Hant.strings","Localizable_ar.strings"]#
    # paths=["Localizable_en.strings","Localizable_zh-Hans.strings"]
    # #开工处理
    # listValue = []
    # wb = xlwt.Workbook()
    # ws = wb.add_sheet('test')
    # listKey = readKeysFromFilePath(paths[0])
    # ws.write(0,0,"Key")
    # for x in range(len(listKey)):
    #     ws.write(x+1,0,listKey[x])
    
    # for y in range(len(paths)):
    #     path = paths[y]
    #     listValue = readValuesFromFilePath(path)
    #     ws.write(0,y+1,path)
    #     for x in range(len(listValue)):
    #         ws.write(x+1,y+1,listValue[x])

    # wb.save("localizableToExcel.xls")

##########################################################
def main():
    # options = addParser()
    # exportToExcel(options)
    exportToExcel()
##########################################################
main()